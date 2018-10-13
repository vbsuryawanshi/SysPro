import sys
import json

class symbolTable:
    def __init__(self):
        self.symbol={}
        self.address=0
        self.types=["dd","db","dw","dq"]
        self.res_types=["resd","resb","resw","resq"]
        self.extern=["global","extern"]
        self.branch=["jmp","loop"]
        self.reg=["eax","ecx","edx","ebx","esp","ebp","esi","edi"]
        self.ins=["mov","add","sub"]


    def get_size(self,val,_type):
        if _type=="dd" or _type=="resd":
            val=map(int,val.split(','))
            return len(val)*4
        elif _type=="db":
             if val[(len(val)-5):]==',10,0':
                 return len(val)-5
             elif val[(len(val)-2):]==',0':
                 return len(val)-3
             else:
                 return len(val)-2
        elif _type=="resb":
            return int(val)
        elif _type=="dq" or _type=="resq":
            val=val.split(',')
            val=map(float,val)
            return len(val)*8


    def get_value(self,val,_type):
        if _type=="dd":
            val=''.join(val)
            val=map(int,val.split(','))
            if len(val)>1:
                return val
            else:
                return val[0]
        elif _type=="dq":
            val=''.join(val)
            val=map(float,val.split(','))
            if len(val)>1:
                return val
            else:
                return val[0]   
        elif _type=="db":
            val=' '.join(val)
            if val[(len(val)-5):]==',10,0':
                val=filter(lambda x:x!="\"",val[:len(val)-5])
                return val
            elif val[(len(val)-2):]==',0':
                val=filter(lambda x:x!="\"",val[:len(val)-2])
                return val
            else:
                val=filter(lambda x:x!="\"",val)
                return val
            
            
    def add(self,a,x):
        self.symbol[a]=x


    def validate(self,x,ad):
        if len(x)>2:
            if x[1] in self.types and x[0] not in self.symbol:
                size=self.get_size(' '.join(x[2:]),x[1])
                self.symbol[x[0]]=[x[1],"D",self.get_value(x[2:],x[1]),size,ad]
                self.address+=size
            elif x[1] in self.res_types and x[0] not in self.symbol:
                size=self.get_size(x[2],x[1])
                self.symbol[x[0]]=[x[1],"D",[],size,ad]
                self.address+=size
            elif x[0] in self.symbol:
                print "\nsymbol <"+x[0]+"> declared more than once"
                sys.exit()
        if len(x)==2:
            if x[0] in self.extern:
                if x[1] not in self.symbol:
                    self.symbol[x[1]]=[x[0],"D",[],"",None]
                else:
                    print "symbol <"+x[1]+"> declared more than once"
                    sys.exit()
                
                
    def display(self):
        print self.symbol

class literal_table:
    def __init__(self):
        self.literal={}
    def display(self):
        print self.literal



class opcode_table:
    def __init__(self):
        self.ins_code=[]
        self.opr_opcode=[]
        self.addr=[]
        self.cmplt_op=[]
        self.addres_op=[]
        self.reg32=["eax","ecx","edx","ebx","esp","ebp","esi","edi"]        
        self.binary=["000","001","010","011","100","101","110","111"]
        with open("instruction.json") as fp:
            self.insCode=json.load(fp)

    def codeGen(self,line,st):
        n=len(line)
        if(n>=3):
            if(n>3):
                line=line[1:]
            self.ins_code+=[self.genInsCode(line[1:],line[0],st)]


    def addReg(self,opcode,reg):
        return map(lambda x:changeCase(x),hex(int(opcode,16)+reg)[2:])


        
    def genInsCode(self,line,ins,s_t):
        n=""
        m=""
        p=""
        if ins=="mov":
            if line[0][:5]=="dword":
                a=sep_var(line[0])
                if a in self.reg32 and line[1] in self.reg32:
                    self.opr_opcode+=[self.insCode[ins][2]]
                    self.addr+=[""]
                    m="00"
                    n=self.binary[(self.reg32.index(line[1]))]
                    p=self.binary[(self.reg32.index(a))]
                elif a in self.reg32 and line[1] not in self.reg32:
                    self.opr_opcode+=[self.insCode[ins][3]]
                    self.addr+=[chn_hex_add(int(line[1]))]
                    m="00"
                    p=self.binary[(self.reg32.index(a))]
                    n="000"
                elif a not in self.reg32 and line[1] in self.reg32:
                    self.opr_opcode+=[self.insCode[ins][2]]
                    self.addr+=["["+st.symbol[a][4]+"]"]
                    m="00"
                    n=self.binary[(self.reg32.index(line[1]))]
                    p="101"
                elif a not in self.reg32 and line[1] not in self.reg32:
                    self.opr_opcode+=[self.insCode[ins][3]]
                    self.addr+=["["+st.symbol[a][4]+"]"+chn_hex_add(int(line[1]))]
                    m="00"
                    p="101"
                    n="000"
            else:
                if (line[0] in self.reg32 and line[1] in self.reg32):
                    self.opr_opcode+=[self.insCode[ins][2]]
                    self.addr+=[""]
                    m="11"
                    n=self.binary[(self.reg32.index(line[1]))]
                    p=self.binary[(self.reg32.index(line[0]))]

                elif line[1][:5]!="dword":
                    self.opr_opcode+=[map(changeCase,(hex(184+self.reg32.index(line[0]))[2:]))]
                    self.addr+=[chn_hex_add(int(line[1]))]
                elif line[1][:5]=="dword":
                    a=sep_var(line[1])
                    if a in self.reg32:
                        self.opr_opcode+=[self.insCode[ins][1]]
                        self.addr+=[""]
                        m="00"  
                        p=self.binary[(self.reg32.index(a))]
                        n=self.binary[(self.reg32.index(line[0]))]
                    elif a not in self.reg32:
                        self.opr_opcode+=[self.insCode[ins][1]]
                        self.addr+=["["+st.symbol[a][4]+"]"]
                        m="00"
                        n=self.binary[self.reg32.index(line[0])]
                        p="101"
            return (m+n+p)             
        elif ins=="add":
            if line[0][:5]=="dword":
                a=sep_var(line[0])
                if a in self.reg32:
                    m="00"
                    if line[1] in self.reg32:
                        n=self.binary[self.reg32.index(line[1])]
                        p=self.binary[self.reg32.index(a)]
                        self.opr_opcode+=[self.insCode[ins][0]]
                        self.addr+=[""]
                    else:
                        n="000"
                        p=self.binary[self.reg32.index(a)]        
                        self.opr_opcode+=[self.insCode[ins][2]]
                        self.addr+=[chn_hex_add(int(line[1]))]
                else:
                    m="00"
                    if line[1] in self.reg32:
                        n=self.binary[self.reg32.index(line[1])]
                        p="101"
                        self.opr_opcode+=[self.insCode[ins][0]]
                        self.addr+=["["+st.symbol[a][4]+"]"]
                    else:
                        n="000"
                        p="101"
                        self.opr_opcode+=[self.insCode[ins][2]]
                        self.addr+=["["+st.symbol[a][4]+"]"+chn_hex_add(int(line[1]))]
            else:
                if line[1][:5]=="dword":
                    a=sep_var(line[1])
                    m="00"
                    if a in self.reg32:
                        self.opr_opcode+=[self.insCode[ins][1]]
                        self.addr+=[""]
                        n=self.binary[self.reg32.index(line[0])]
                        p=self.binary[self.reg32.index(a)]
                    else:
                        self.opr_opcode+=[self.insCode[ins][1]]
                        self.addr+=["["+st.symbol[a][4]+"]"]
                        p='101'
                        n=self.binary[self.reg32.index(line[0])]
                elif line[1] in self.reg32:
                    m="11"
                    self.opr_opcode+=[self.insCode[ins][0]]
                    self.addr+=[""]
                    n=self.binary[self.reg32.index(line[1])]
                    p=self.binary[self.reg32.index(line[0])]
                else:
                    m="11"
                    self.opr_opcode+=[self.insCode[ins][2]]
                    self.addr+=[chn_hex_add(int(line[1]))]
                    n="000"
                    p=self.binary[self.reg32.index(line[0])]
            return (m+n+p)        
        elif ins=="sub":
            if line[0][:5]=="dword":
                a=sep_var(line[0])
                if a in self.reg32:
                    m="00"
                    if line[1] in self.reg32:
                        n=self.binary[self.reg32.index(line[1])]
                        p=self.binary[self.reg32.index(a)]
                        self.opr_opcode+=[self.insCode[ins][0]]
                        self.addr+=[""]
                    else:
                        n="101"
                        p=self.binary[self.reg32.index(a)]        
                        self.opr_opcode+=[self.insCode[ins][2]]
                        self.addr+=[chn_hex_add(int(line[1]))]
                else:
                    m="00"
                    if line[1] in self.reg32:
                        n=self.binary[self.reg32.index(line[1])]
                        p="101"
                        self.opr_opcode+=[self.insCode[ins][0]]
                        self.addr+=["["+st.symbol[a][4]+"]"]
                    else:
                        n="101"
                        p="101"
                        self.opr_opcode+=[self.insCode[ins][2]]
                        self.addr+=["["+st.symbol[a][4]+"]"+chn_hex_add(int(line[1]))]
            else:
                if line[1][:5]=="dword":
                    a=sep_var(line[1])
                    m="00"
                    if a in self.reg32:
                        self.opr_opcode+=[self.insCode[ins][1]]
                        self.addr+=[""]
                        n=self.binary[self.reg32.index(line[0])]
                        p=self.binary[self.reg32.index(a)]
                    else:
                        self.opr_opcode+=[self.insCode[ins][1]]
                        self.addr+=["["+st.symbol[a][4]+"]"]
                        p='101'
                        n=self.binary[self.reg32.index(line[0])]
                elif line[1] in self.reg32:
                    m="11"
                    self.opr_opcode+=[self.insCode[ins][0]]
                    self.addr+=[""]
                    n=self.binary[self.reg32.index(line[1])]
                    p=self.binary[self.reg32.index(line[0])]
                else:
                    m="11"
                    self.opr_opcode+=[self.insCode[ins][2]]
                    self.addr+=[chn_hex_add(int(line[1]))]
                    n="101"
                    p=self.binary[self.reg32.index(line[0])]
            return (m+n+p)   


    def convertToHex(self,x):
        for i in range(len(x)):
            if x[i]!='' and x[i]!=None:
                h=hex(int(x[i],2))[2:]
                if(len(h)==1):
                    x[i]="0"+h
                else:
                    x[i]=h
        return x 
        
    def display(self):
        l=zip(map(lambda x:''.join(x),self.opr_opcode),self.convertToHex(self.ins_code),self.addr)
        self.cmplt_op=map(lambda (x,y,z):x+y+z,l)
        curr_add="00000000"
        for i in self.cmplt_op:    
            self.addres_op+=[curr_add]     
            a=len(i)
            if("[" in i):
                a=a-2
            a=a/2
            curr_add=chn_hex_add(int(curr_add,16)+a)
        print "\n"
        for i in range(len(self.cmplt_op)):
            print (self.addres_op[i],self.cmplt_op[i])
            

def changeCase(x):
    if x in "abcdef":
        return chr(ord(x)-32)
    return x  

        
def add_literal(lt,val):
    if val[0]=='"':
        if val[0]=='"' and val[-1]=='"':
            lt.literal[val[1:len(val)-1]]=["char",len(val)-2]
    elif is_num(val):
            lt.literal[val]=['int',4]
    else:
        print "invalid literal <"+val+">"
        sys.exit()
        
    
def sep_var(x):
    x=''.join((''.join(x.split('dword[')).split(']')))
    x=''.join((''.join(x.split('byte[')).split(']')))
    return x

def concat_list(x):
    return [i for j in x for i in j]

def chn_hex_add(x):
     he_x=hex(x)[2:]
     c_ad=("0"*(8-len(he_x)))+ he_x
     return c_ad
    
def seperate(line):
    n=len(line)
    if n==1:
        line[0]=line[0].split(":")
        line=concat_list(line)
        line=filter(lambda x:x!='',line)
        return line
    elif n==2:  
        if ":" in line[0]:
            line[0]=line[0].split(":")
            line[1]=line[1].split(",")
            line=concat_list(line)
            line=filter(lambda x:x!='',line)
            return line
        else:
            line[0]=line[0].split(' ')
            line[1]=line[1].split(',')
            line=concat_list(line)
            line=filter(lambda x:x!='',line)
            return line
    elif n==3:
        line[0]=line[0].split(":")
        line[2]=line[2].split(",")
        line[1]=line[1].split(" ")
        line=concat_list(line)
        line=filter(lambda x:x!='',line)
        return line

def is_alpha(x):
    a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x[0] in a:
        return 1
    else:
        return 0


def is_num(x):
    a="0123456789"
    A=filter(lambda y:y in a,x)
    if x==A:
        return 1
    return 0
    
def validate_instructions(lines,st,lt,i):
    flag1=0
    flag2=0
    line=lines[i]
    n=len(line)
    if n==1:
        if line[0]!="ret" or line[0]!="main":
            if line[0] not in st.symbol:
                st.symbol[line[0]]=["func","D","",-1]
            else:
                print " >loop <"+line[0]+"> already exists"
                sys.exit()
    elif n==2:
        if line[0] in st.branch:
            if line[1] not in st.symbol and line[1]!="ret":
                st.symbol[line[1]]=["func","U","",-1]
                
    elif n==3:
        if line[1][:6]=="dword[" and line[2][:6]=="dword[":
            print "> memory to memory transfer not possible or something invalid"
            sys.exit()
        elif line[1][:6]=="dword[":
            flag1=1
        elif line[2][:6]=="dword[":
            flag2=1
        line=map(sep_var, line)
        if line[0] in st.ins:
            if line[1] not in st.reg and line[2] not in st.reg and flag1!=1:
                print "> memory to memory transfer not possible or something invalid"
                sys.exit()
            elif line[1] in st.reg:
                if is_alpha(line[2]) and line[2] not in st.symbol and line[2] not in st.reg and flag2==1:
                    print ">symbol <"+line[2]+">  used but not defined"
                    sys.exit()
                elif line[2] not in st.symbol and line[2] not in st.reg and flag2==0:
                    add_literal(lt,line[2])
            elif line[2] in st.reg:
                if is_alpha(line[1]) and line[1] not in st.symbol and line[1] not in st.reg and flag1==1:
                    print "__>symbol <"+line[1]+"> used but not defined"                    
                    sys.exit()
                elif line[1] not in st.symbol and line[1] not in st.reg and flag1==0:
                    add_literal(lt,line[1])
                    
             
        else:
            print "invalid instruction <"+line[0]+">"
            sys.exit()
    elif n==4:
        if line[2][:6]=="dword[" and line[3][:6]=="dword[":
            print "__> memory to memory transfer not possible or something invalid"
            sys.exit()
        elif line[2][:6]=="dword[":
            flag1=0
        elif line[3][:6]=="dword[":
            flag2=0
        line=map(sep_var,line)
        if line[0] not in st.symbol:
            st.symbol[line[0]]=["func","D","",-1]
            if line[1] in st.ins:
                if line[2] not in st.reg and line[3] not in st.reg:
                    print "__> memory to memory transfer not possible or something invalid"
                    sys.exit()
                if line[2] in st.reg:
                    if is_alpha(line[3]) and line[3] not in st.symbol and  line[3] not in st.reg and flag1==1:
                        print "__>symbol <"+line[3]+">  used but not defined"
                        sys.exit()
                    elif line[3] not in st.symbol and  line[3] not in st.reg and flag1==0:
                        add_literal(lt,line[3])
                elif line[3] in st.reg:
                    if is_alpha(line[2]) and line[2] not in st.symbol and line[3] not in st.reg and flag2==1:
                        print "__>symbol <"+line[2]+">  used but not defined"
                        sys.exit()
                    elif line[2] not in st.symbol and line[3] not in st.reg and flag2==0:
                        add_literal(lt,line[2])   
            else:
                print "invalid instruction <"+line[0]+">"
                sys.exit()
        else:
            if st.symbol[line[0]][1]=="D":
                print"__> symbol as label <"+line[0]+"> redefined"
                sys.exit()
            elif st.symbol[line[0]][1]=="U":
                st.symbol[line[0]][1]='D'
            
     
#mov eax,ebx          

filename=input("enter the file name:")
fp=open(filename,"r+")
text=fp.read()
lines=filter(lambda w:w!=[],map(lambda y:filter(lambda z:z!='',y),map(lambda x:x.split(' '),text.split("\n"))))
lines=map(lambda x:map(lambda y:filter(lambda z:z!='\t',y),x),lines)
st=symbolTable()
lt=literal_table()
ot=opcode_table()
k=None
current_ad="00000000"
for line in lines:
    if line[0].split(':')[0]!="main":
        if(line[0]=="section"):
            current_ad="00000000"
            st.address=0
        current_ad=chn_hex_add(st.address)
        st.validate(line,current_ad)
    else:
        current_ad="00000000"
        k=line
        
index=lines.index(k)
lines=lines[index:]


#change first one where main is starting (no insrtuction should be there after main: on the same line)

lines=map(seperate,lines)
for i in range(1,len(lines)):
    
    validate_instructions(lines,st,lt,i)
    ot.codeGen(lines[i],st)

print "\nSYMBOL TABLE\n"
st.display()
print "\nLITERAL TABLE\n"
lt.display()
print "\nOPCODE TABLE\n"    
ot.display()

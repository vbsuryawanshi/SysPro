import regTable
import symTable

def findAttr():
    fp=open("test.asm","r")
    name=size=ts=0
    dict={}
    dindx=0
#    print("Name\tSize\tTSize\tSymbol/Lable\tDefine\tAddr\tContent")
    ddcnt=ddnt=dbcnt=dbnt=cnt=dqnt=dqcnt=0
    for i in fp:
        arr=i.split(" ")
        for j in range(len(arr)):
            if arr[j]=='dd':
                name=arr[j-1].strip()
                size=4
                ddnt+=1
                cnta=arr[j+1].split(",")
                ddcnt+=int(len(cnta))
                dindx+=1
                symtable(dict,dindx,name,size,ddcnt,'S','D',ts,cnta)
                ts+=ddcnt*int(size)
            elif arr[j]=='db':
                name=arr[j-1].strip()
                size=1
                dbnt+=1
                arr1=arr[j+1:]
                for k in range(len(arr1)):
                    for l in range(len(arr1[k])):
                        if arr1[k][l]=='"' or arr1[k][l]=="'":
                            cnt+=1
                        elif cnt==1 and arr1[k][l]!='\n\t':
                            dbcnt+=1
                        elif cnt==2 or cnt==0:
                            if arr1[k][l]!=',' and arr1[k][l]!='1' and arr1[k][l]!='\n':
                                dbcnt+=1
                if k>0:
                    dbcnt+=1
                dindx+=1
                symtable(dict,dindx,name,size,dbcnt,'S','D',ts,arr1)
                ts+=dbcnt*int(size)
            elif arr[j]=='dq':
                dqnt+=1
                cta=arr[j+1].split(",")
                dqcnt+=int(len(cta))
        
        regTable.regT(arr)

    #findLables(dict,dindx)    
    #printTable(dict)
    fp.close()

def checklable(lablecol):
    fp=open("test.asm","r")
    for i in fp:
        index=i.find("jmp")
        if index>-1:
            print(i[index])
    fp.close()
       

def findLables(dict,dindx):
    lablecol=[[]]
    j=0
    fp=open("test.asm","r")
    for i in fp:
        index=i.find(':')
        err=i.find('"')
        if index>-1 and err==-1:
            label=(i[:index].strip())
            x=label.split(' ')
            dindx+=1
            symtable(dict,dindx,x[1],0,0,'L','D',int(x[0]),'-')
    fp.close()

def symtable(dict,dindx,name,size,tsize,sym,define,addr,cont):
    dict1={dindx:{'Symname':name,'Size':size,'Tsize':tsize,'Sym/Label':sym,'Define':define,'Addr':addr,'Content':cont}}
    dict.update(dict1)

def printTable(dict):
    for s_id,sym_info in dict.items():
        print("\nS_id:",s_id)
        for key in sym_info:
            print(key+':'+str(sym_info[key]))

findAttr()
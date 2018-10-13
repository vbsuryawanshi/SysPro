import re
import litTable
import symTable

reg_op={'Reg#0':'000','Reg#1':'001','Reg#2':'010','Reg#3':'011','Reg#4':'100','Reg#5':'101','Reg#6':'110','Reg#7':'111'}
mov={'r32,imm32':'B8','r32,r/m32':'8B','r/m32,r32':'89','r/m32,imm32':'C7'}
add={'r/m32,imm':'83','r/m32,r32':'01','r32,r/m32':'03'}

def modRm(opcode,sreg,dreg):
    no=""
    no+=opcode
    no+=sreg
    no+=dreg
    return hex(int(no,2))[2:]   #int(x[, base])->integer

def cal_op(instrn,arr,rcnt,scnt,lcnt):
    sreg=dreg=addr=""
    fst=-1
    flag=-1
    if len(arr)>1:
        fst=arr[0].find("[")
        if fst>-1:
            flag=0
        else:
            fst=arr[1].find("[")
            if fst>-1:
                flag=1
            else:
                flag=-1
    if rcnt==2:
        for key,val in reg_op.items():
                if key==arr[1]:
                    sreg=val
                if key==arr[0]:
                    dreg=val
                    continue
        if instrn=="mov":
            rval=modRm("11",sreg,dreg)
            return '89'+rval
        elif instrn=="add":
            rval=modRm("11",sreg,dreg)
            return '01'+rval
    elif rcnt==1 and scnt==1:
        if flag!=-1:
            if flag==0:
                for key,val in reg_op.items():
                    if key==arr[1]:
                        sreg=val
                        break
                addr=symTable.checkSym_opcode((arr[0][fst+1:]).strip("]"))
            elif flag==1:
                for key,val in reg_op.items():
                    if key==arr[0]:
                        sreg=val
                        break
                addr=symTable.checkSym_opcode((arr[1][fst+1:]).strip("]"))
            if instrn=="mov":
                if key!='Reg#0':
                    rval=modRm("00",sreg,"101")
                    return '8b'+rval+'['+addr+']'
                else:
                    return 'a1'+'['+addr+']'
            elif instrn=="add":
                rval=modRm("00",sreg,"101")
                return '03'+rval+'['+addr+']'  
    elif rcnt==1 and lcnt==1:
        for key,val in reg_op.items():
                if key==arr[0]:
                    dreg=val
                    break
        sreg=litTable.checkLit_opcode(arr[1])            
        if instrn=="mov":
            rval=str((10111000+int(dreg)))
            rval=hex(int(rval,2))[2:]
            return rval+sreg
        elif instrn=="add":
            rval=modRm("11","000",dreg)
            return '83'+rval+sreg
    else:
        return "0"

import symTable
import litTable
import re

reg={'eax':'Reg#0','al':'Reg#0','ecx':'Reg#1','edx':'Reg#2','ebx':'Reg#3','esp':'Reg#4','ebp':'Reg#5','esi':'Reg#6','edi':'Reg#7'}
fp=open("intermediate.txt","a")
def regT(instrn,dindx,lindx):
    flag=valflag=0
    i=len(instrn)
    if i>1:
        m=bool(re.search('printf',instrn[1].strip(),re.IGNORECASE))
        if m==True:
            fp.writelines(instrn)
        for key in reg:
            val=instrn[1].__contains__(key)
            if val==True:
                valflag=1
                str1=""
                str1+=instrn[0].strip()+' '
                chk=instrn[1].strip().split(",")
                for j in range(len(chk)):
                    fst=chk[j].find('[')
                    if j==0:
                        if key==chk[j].strip():
                            str1+=reg.get(key)
                        elif chk[j].__contains__(key) and fst>-1:
                            str1+=chk[j][:fst+1]+reg.get(key)+']'
                        else:
                            indx=""
                            indx=symTable.checkSym(chk[j].strip())
                            str1+=indx+'\n'
                        if(len(chk)==1):
                            fp.write(str1+'\n')
                    elif j>0:
                        for r in reg:
                            if r==chk[j].strip():
                                str1+=','+reg.get(r)+'\n'
                                flag=1
                                break
                            elif chk[j].__contains__(key) and fst>-1:
                                str1+=chk[j][:fst+1]+reg.get(key)+']'+'\n'
                                flag=1
                                break
                            else:
                                flag=0
                        if flag==0:
                            indx=""
                            indx=symTable.checkSym(chk[j].strip())
                            if indx!=chk[j].strip():
                                str1+=','+indx+'\n' 
                            else:
                                indx=litTable.checkLit([chk[j].strip()])
                                if indx==-1:
                                    lindx+=1
                                    indx=litTable.litT(lindx,[chk[j].strip()],1)
                                str1+=','+indx+'\n'
                        fp.writelines(str1)
                break
        if valflag==0:
            indx=str1=""
            indx=symTable.checkSym(instrn[1].strip())
            if indx!=(instrn[1].strip()):
                str1=instrn[0].strip()+' '+indx+'\n'
                fp.writelines(str1)
            else:
                if instrn[0].strip()=='jz' or instrn[0].strip()=='jmp':
                    dindx+=1
                    symTable.symT(dindx,instrn[1].strip(),0,0,'L','U','-','-')
                    indx=symTable.checkSym(instrn[1].strip())
                    if indx!=(instrn[1].strip()):
                        str1=instrn[0].strip()+' '+indx+'\n'
                        fp.writelines(str1)
    else:
        str1=""
        if instrn[0]!='\n':
            str1+=instrn[0]
            fp.write(str1)
            
    return dindx,lindx
def findAttr():
    fp=open("test.asm","r")
    name=size=ts=0
    print("Name\tSize\tTSize\tSymbol/Lable\tDefine\tAddr\tContent")
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
                printTable(name,size,ddcnt,'S','D',ts,cnta)
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
                printTable(name,size,dbcnt,'S','D',ts,arr1)
                ts+=dbcnt*int(size)
            elif arr[j]=='dq':
                dqnt+=1
                cta=arr[j+1].split(",")
                dqcnt+=int(len(cta))

    #print("Db %d"%dbnt,dbcnt)
    #print("Dd %d"%ddnt,ddcnt)
    #print("Dq %d"%dqnt,dqcnt)
    fp.close()

def checklable(lablecol):
    fp=open("test.asm","r")
    for i in fp:
        index=i.find("jmp")
        if index>-1:
            print(i[index])
    fp.close()
       

def findLables():
    lablecol=[[]]
    j=0
    fp=open("test.asm","r")
    for i in fp:
        index=i.find(':')
        err=i.find('"')
        if index>-1 and err==-1:
            label=(i[:index].strip())
            x=label.split(' ')
            printTable(x[1],0,0,'L','D',int(x[0]),'-')
    fp.close()

def printTable(name,size,tsize,sym,define,addr,cont):
    print("%s\t%d\t%d\t\t%c\t%c\t%d\t%s"%(name,size,tsize,sym,define,addr,cont))

findAttr()
findLables()

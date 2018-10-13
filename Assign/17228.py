import chartoascii
import keyword
err={1:"ERROR 0:Digits are not ALLOWED",2:"ERROR 1:Space are not ALLOWED"}

dic=[]
dic=['Vaibhav','Va ibh av','va12bh']

def validname(name):
    for bit in name:
        if bit.isalpha():
            val=0
        elif bit==' ':
            val=1
            break
        else:
            val=2
            break
    return val

def chartoascii(str1):
    s=""
    for i in range(len(str1)):
        a=(hex(ord(str1[i]))).strip('0x')
        s+=a
    print(s)

def check():
    for i in range(len(dic)):
        rval=validname(dic[i])
        chartoascii(dic[i])
        if(rval==1):
            print(err[2])
        elif(rval==2):
            print(err[1])
        elif(rval==0):
            print("")

check()

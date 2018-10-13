import time
import binascii
str1=b"This is a String"
a=binascii.hexlify(str1)
b=str(a,'ascii')
print(b)

str1='"Addition is %d",10,0'
sr=''.join(hex(ord(c))[2:] for c in str1)
print(sr)
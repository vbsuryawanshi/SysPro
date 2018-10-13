def con(st):
    s=""
    for i in range(len(st)):
        a=(hex(ord(st[i]))).strip('0x')
        s+=a
    print(s)

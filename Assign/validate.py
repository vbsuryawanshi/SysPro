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

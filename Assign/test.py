import array

arr=array.array('i',[1,2,2])
for i in range(0,len(arr)):
    print(arr[i])

a='a'
b=int(5)

print("%s\t%d"%(a,b))


m=[[1,2,3],[4,5,6],[7,8,9]]
mm=[m[diag][diag] for diag in [0,1,2]]
print(mm)
        
#    mm.append(m[i][1])
#print(m[0][1])
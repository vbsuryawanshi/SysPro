"""seq=('Symname','Size','Tsize','Sym/Label','Define','Addr','Content')
#dict={'Symname':'a','Size':4,'Tsize':1,'Sym/Label':'S','Define':'D','Addr':0,'Content':'Hiiiiii'}
dict=dict.fromkeys(seq)
print(dict)
val=(dict.get('Symname'))
dict['Symname']='b'
dict.update(dict)
print(dict)"""

import time
st=time.time()
dict={1:{'Symname':'b','Size':4,'Tsize':1,'Sym/Label':'S','Define':'D','Addr':0,'Content':'Hiiiiii'}}
dict1={2:{'Symname':'a','Size':1,'Tsize':4,'Sym/Label':'S','Define':'D','Addr':4,'Content':'Vaibhav'}}
dict.update(dict1)

for s_id,sym_info in dict.items():
    print("\nS_id:",s_id)
    for key in sym_info:
        if sym_info[key]=='a':
            print(key+':'+sym_info[key])
            break

print(st-time.time())
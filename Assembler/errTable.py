#jmp pqr but cant defined = error: symbol 'pqr' undefined
#mov eaz,any = error: invalid combination of opcode and operands
#push except spell mistake = error: parser: instruction expected

errors={'section':'error: parser: instruction expected','dd':'error: parser: instruction expected','db':'error: parser: instruction expected','dq':'error: parser: instruction expected','global':'error: parser: instruction expected','extern':'error: parser: instruction expected'}
def findErr(instrn):
    instrn=instrn.lower()
    flag=0
    for key,value in errors.items():
        if instrn==key:
            flag=1
section .data
	str1 db "*!@#$%^&({[|]})\/<?>",0
	len equ $-str1
	nl db 10,0
	
section .bss
	ecnt resd 1
	dcnt resd 1
	str2 resb len

section .text
	global main
	
main:	

	mov esi,str1
	mov edi,str2
	mov ecx,len
	mov dword[ecnt],2
	mov dword[dcnt],1
pqr:	lodsb
	stosb
	loop pqr
	jmp pnt

again:	xor esi,esi
	xor edi,edi
	
	mov esi,str1
	mov edi,str2
	mov ecx,len
	sub ecx,dword[ecnt]
	add edi,dword[dcnt]
	add dword[ecnt],1
	add dword[dcnt],1
stu:	lodsb
	cmp al,''
	je end     ;main insted of end for continues loop
 	stosb
	loop stu
	mov edi,str2
	mov ecx,dword[ecnt]
	sub ecx,2
stu1:	lodsb
	stosb
	loop stu1
	
pnt:	mov eax,4
	mov ebx,1
	mov ecx,str2
	mov edx,len
	int 0x80

	mov eax,4
	mov ebx,1
	mov ecx,nl
	mov edx,1
	int 0x80
	jmp again
	
end:

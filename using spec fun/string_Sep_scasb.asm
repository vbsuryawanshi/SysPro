section .data
	a db "First,second,Third",0
	len equ $-a
	
section .text
	global main

main:
	xor eax,eax
	mov edi,a
	mov al,','
	mov ecx,len 
	repne scasb	;scan byte by byte
	;nop		;no operation
	mov edx,ecx
	mov esi,edi
	repne scasb
	sub edx,ecx
	dec edx
	
	mov eax,4
	mov ebx,1
	mov ecx,esi
	int 0x80	;interrupt

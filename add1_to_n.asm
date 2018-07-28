section .data
	msg db "%d",0
	msg1 db "addition is %d",10,0	;10 for \n and 0 for \0
section .bss
	n resd 1
section .text
	global main
	extern printf,scanf
main:	push n
	push msg
	call scanf
	add esp,8	;esp is a stack pointer
	mov ecx,dword[n]
	xor edx,edx
;pqr:	cmp ecx,0
;	jz abc		;j(conditional) 
;	add edx,ecx
;	dec ecx
;	jmp pqr
pqr:	add edx,ecx
	loop pqr	
abc:	push edx
	push msg1
	call printf
	add esp,8
	

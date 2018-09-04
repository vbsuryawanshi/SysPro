section .data
	First db "This is the string",0
	Second db "This is the another string",10,0
	nl db 10,0
;	len equ $-First

section .bss
	Third resb 30

section .text
	global main
	extern puts
main:
;	mov ecx,len
	mov eax,First
	xor ecx,ecx
pqr:	cmp byte[eax],0
	jz final
	inc eax
	inc ecx
	jmp pqr

final:	mov ebx,First
	add ebx,ecx
	mov edx,Third
	inc ecx
	push ecx

ttt:	xor eax,eax
	mov al,byte[ebx]	;al register is used for store 1 byte
	mov byte[edx],al
	dec ebx
	inc edx
	loop ttt
	
	pop ecx
	mov edx,ecx
	mov eax,4
	mov ebx,1
	mov ecx,Third
	int 0x80
	
	mov eax,4
	mov ebx,1
	mov ecx,nl
	mov edx,2
	int 0x80

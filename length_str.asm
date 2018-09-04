section .data
	First db "First String",0
	msg db "length is %d",10,0
section .text
	extern printf
	global main
main:
	mov esi,First
	xor eax,eax
	mov al,0
	xor ecx,ecx

lp:	cmp byte[esi],0
	jz tst
	inc ecx
	inc esi
	jmp lp

tst:	push ecx
	push msg
	call printf
	add esp,8

section .data
	First db "First String",0
	F_len equ $-First
	Second db "First String",0

section .text
	global main
main:	mov esi,First
	mov edi,Second
	mov ecx,F_len
	rep cmpsb
	
;	push Third
;	call puts
;	add esp,4


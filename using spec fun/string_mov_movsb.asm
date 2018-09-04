section .data
	First db "First String",0
	F_len equ $-First
	Second db "Second String",0
	S_len equ $-Second
	
section .bss
	Third resb F_len
	Fourth resb S_len

section .text
	global main
	extern puts
	
main:	mov esi,First
	mov edi,Third
	mov ecx,F_len
	rep movsb	;rep:(repeate) movsb:(ecx is dec & esi,edi is inc)
	push Third
	call puts
	add esp,4
	
	;DF is a direction flag and its bydefault 0
	;std is use to set direction flag
	;movsb->mov strign byte 

section .data
	First db "First string",0

section .bss
	Snd resb 20

section .text
	global main
	extern puts
	
main:	mov esi,First
	mov edi,Snd
	cld
	mov al,byte[esi]
	std
	mov byte[edi],al
	movsb

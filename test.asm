section .data
string db "This is our first string program",10,0
len equ $-string
section .rodata
msg db "counter is %d",10,0
section .bss
counter resd 1
section .text
global main
extern printf,puts
main:
	mov edi,string
	

%macro add 2
	mov eax,%1
	sub eax,%2
%endmacro

section .text
	global main

main:
	add 10,20
	add eax,eax
	add edx,10
	add 10,eax

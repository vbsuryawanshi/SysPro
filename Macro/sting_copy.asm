%macro str 2
	mov eax,%1
	mov ebx,%2
	lodsb
	stosb
%endmacro

section .data
	str1 db "First String",10,0
	len equ $-str1

section .bss
	str2 resb len

section .text
	global main
	
main:
	mov esi,str1
	mov ecx,len
	mov edi,str2
pqr:	str esi,edi
	loop pqr
	
	mov eax,4
	mov ebx,1
	mov ecx,str2
	mov edx,len
	int 0x80

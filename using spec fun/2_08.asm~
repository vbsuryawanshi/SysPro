section .data
	first db 10,"source string",10
	len equ $-first
section .bss
	snd resb len
section .text
	global main

main:
	mov esi,first
	mov ecx,len
	mov edi,snd
	xor eax,eax
	add esi,ecx
	dec esi
pqr:	std		;decrement
	lodsb		;;load string byte by byte al=esi and then esi++ but std dec std
	cld		;increment
	cmp al,''
	jz go
	cmp al,10
	jz end
go:	sub al,32

end:	stosb		;store string byte by byte edi=al 
	loop pqr
	
	mov eax,4
	mov ebx,1
	mov ecx,snd
	mov edx,esi
	int 0x80

section .data
	first db "source string",10
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

pqr:	lodsb		;;load string byte by byte al=esi and then esi++ but std dec std
	cmp al,''
	jz end1
	cmp al,10
	jz end
	cmp al,' '
	jz end
	sub al,32

end:	stosb		;store string byte by byte edi=al 

	lodsb
	stosb
	loop pqr
	
end1:	mov eax,4
	mov ebx,1
	mov ecx,snd
	mov edx,esi
	int 0x80
	
;	jmp main	

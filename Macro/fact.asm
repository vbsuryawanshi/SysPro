%macro fact 2
	mov eax,%1
	mov ebx,%2
	mul ebx
%endmacro

section .data
	n dd 5,0
	op dd "%d",10,0
		
section .text
	global main
	
main:
	mov esi,dword[n]
	mov edi,dword[n]
pqr:	cmp edi,0
	je end
	sub edi,1
	fact esi,edi
	sub esi,1
	jmp pqr
end:

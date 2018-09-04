section .bss
	First resd 1
	Second resd 1
section .text
	global main
main:
	mov dword[First],100
	mov dword[Second],35
	mov eax,dword[First]
	mov ebx,first
	xor edx,edx	;make this 0 becz it gives floating point exception and edx store reminder
	div dword[Second]

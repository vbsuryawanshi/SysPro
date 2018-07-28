section .data
	arr dd 10,24,39,7,48,-1
	msg db "Addition is %d",10,0
section .bss
	sum resd 1
	four resd 1
section .text
	global main
	extern printf
main:	mov dword[sum],0	;dword[sum] i.e. sum jya address la ahe tithe value mhnun 0 store
	xor ecx,ecx		;ecx is a index of arr
	mov dword[four],4
abc:	mov esi,arr
	mov eax,dword[four]
	mul ecx			;eax=eax*ecx
	add esi,eax
	cmp dword[esi],-1
	jz pqr
	mov edx,dword[esi]
	add dword[sum],edx
	inc ecx
	jmp abc
pqr:	push dword[sum]
	push msg
	call printf
	add esp,8

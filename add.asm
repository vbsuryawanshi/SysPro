section .data
	a db "Addition is %d",10,0
section .text
	global main
	extern puts,printf
main:	xor eax,eax
	xor ebx,ebx
	xor ecx,ecx
	xor edx,edx
	mov eax,20
	mov ebx,30
	add eax,ebx
	push eax
	push a
	call printf
	add esp,8

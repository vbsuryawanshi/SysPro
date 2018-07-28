section .data
	a db "My first prog",10,0
section .text
	global main
	extern puts
main:	xor eax,eax
	xor ebx,ebx
	xor ecx,ecx
	xor edx,edx
	mov eax,20
	mov ebx,30
	mov ecx,40
	mov edx,50
	push a
	call puts
	add esp,4

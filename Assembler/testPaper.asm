section .data
	First db "This is the string",0
	Second db "This is the another String",10,0
	nl db 10,0

section .text
	global main
	extern puts
	
main:
	mov eax,First
	xor ecx,ecx
	inc eax
	inc ecx
	mov ebx,Second
	add ebx,ecx
	mov edx,First
	inc ecx
	push ecx
	xor eax,eax
	dec ebx
	inc edx
	pop ecx
	mov edx,ecx
	mov eax,4
	mov ebx,1
	mov ecx,First
	int 0x80

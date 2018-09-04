section .data
	Matrix1 dd 10,20,30
		dd 40,50,60
		dd 70,80,90
	Matrix2	dd 10,20,30
		dd 40,50,60
		dd 70,80,90
	op dd "%d ",10,0

section .bss
	result resd 9
	extern printf
section .text
	global main

main:	mov edi,9
	xor ecx,ecx
lp:	mov edx,result
	push edx
	xor edx,edx
	mov eax,4
	mul ecx
	mov ebx,Matrix2
	mov esi,Matrix1
	add esi,eax
	add ebx,eax
	pop edx
	add edx,eax
	pusha
	mov ecx,dword[esi]
	add ecx,dword[ebx]
	mov dword[edx],ecx
	push dword[edx]
	push op
	call printf
	add esp,8
	popa
	inc ecx
	dec edi
	cmp edi,0
	jnz lp
	
	

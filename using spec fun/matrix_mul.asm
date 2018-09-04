section .data
	Matrix1 dd 1,2,3
		dd 40,50,60
		dd 70,80,90
	Matrix2	dd 1,20,30
		dd 4,50,60
		dd 7,80,90
	op dd "%d ",10,0

section .bss
	result resd 9
	cnt resd 1
	extern printf
section .text
	global main

main:	mov edi,9
	xor ecx,ecx
lp:	mov dword[cnt],2
	mov edx,result
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
	mov eax,dword[ebx]
	push edx
	mul ecx
	pop edx
	mov dword[edx],eax
	push edx
	
next:	mov ebx,Matrix2
	mov esi,Matrix1
	mov ecx,dword[cnt]
	mov eax,4
	mul ecx
	add esi,eax
	mov ecx,3
	mov eax,eax
	mul ecx
	add ebx,eax
	mov ecx,dword[esi]
	mov eax,dword[ebx]
	mul ecx
	pop edx
	add dword[edx],eax
	push edx
	mov ecx,dword[cnt]
	dec ecx
	mov dword[cnt],ecx
	cmp ecx,0
	jnz next
	
	push dword[edx]
	push op
	call printf
	add esp,8
	popa
	inc ecx
	dec edi
	;cmp edi,0
	;jnz lp
	
	

	mov edi,9
	xor ecx,ecx
lp:	mov eax,4
	mul ecx
	mov esi,Matrix1
	add esi,eax
	pusha
	push dword[esi]
	push msg
	call printf
	add esp,8
	popa
	inc ecx
	dec edi
	cmp edi,0
	jnz lp
	
	
	


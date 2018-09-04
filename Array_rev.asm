section .data
	ip db "%d",0
	op db "%d",10,0
	msg db "Reverse array is :",10,0

section .bss
	arr resd 100
	n resd 1
	temp resd 1
section .text
	global main
	extern printf,scanf
	
main:
	push n
	push ip
	call scanf
	add esp,8

	xor ecx,ecx
	xor esi,esi
loop:	mov esi,arr
	cmp ecx,dword[n]
	je jump
	mov eax,4
	mul ecx
	push ecx
	add esi,eax
	push esi
	push ip
	call scanf
	add esp,8
	pop ecx
	inc ecx
	jmp loop
	
jump:	xor ebx,ebx
	xor edi,edi
	sub ecx,1
again:	mov esi,arr
	cmp ecx,edi
	jle print
	mov eax,4
	mul ecx
	push ecx
	add esi,eax
	mov ebx,dword[esi]
	push ebx
	
	mov esi,arr
	mov eax,4
	mul edi
	add esi,eax
	mov eax,dword[esi]
	mov dword[temp],eax
	pop ebx
	mov dword[esi],ebx 	;last to first pos
	
	mov esi,arr
	pop ecx
	mov eax,4
	mul ecx
	push ecx
	add esi,eax
	mov eax,dword[temp]
	mov dword[esi],eax
	
	inc edi
	pop ecx
	dec ecx
	jmp again
	
print:	xor edi,edi
	xor ecx,ecx
;	push msg
;	call printf
;	add esp,4
	
loop1:	mov esi,arr
	cmp ecx,dword[n]
	je end
	mov eax,4
	mul ecx
	push ecx
	add esi,eax
	push dword[esi]
	push op
	call printf
	add esp,8
	pop ecx
	inc ecx
	jmp loop1
	
end:
	

section .data
	msg db "Max number is %d",10,0
	msg1 db "Enter the value of n:",0
	acc db "%d",0
section .bss
	n resd 1
	arr resd 100
	max resd 1
	ip resd 1
section .text
	global main
	extern printf,scanf
main:	pusha
	push msg1
	call printf
	add esp,4
	push n
	push acc
	call scanf
	add esp,8
	popa
	
	xor ecx,ecx
	xor esi,esi
loop:	mov esi,arr
	cmp ecx,dword[n]
	je calculate
	mov eax,4
	mul ecx
	add esi,eax
	push ecx
	push esi
	push acc
	call scanf
	add esp,8
	pop ecx
	inc ecx
	jmp loop
	
calculate:
	mov ebx,dword[n]
	mov dword[max],0
	xor ecx,ecx
	xor edi,edi
	mov edi,dword[max]
	
again:	mov esi,arr
	mov eax,4
	mul ecx
	add esi,eax
	cmp edi,dword[esi]
	jg reasign    			
	inc ecx
	dec ebx
	mov edi,dword[esi]
	cmp ebx,0
	jne again
	jmp end

reasign:
	inc ecx
	dec ebx
	cmp ebx,0
	je end
	jmp again
	
end:	push edi
	push msg
	call printf
	add esp,8

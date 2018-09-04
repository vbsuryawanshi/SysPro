section .data
	First db '17228,vaibhav,m,msc',0
	      db '17219,ashish,f,msc',0
	      db '17218,vaibhav,m,msc',10,0
	nl db 10,0

section .bss
	cnt resd 1
	Third resb 100

section .text
	global main

main:	enter 0,0
	mov eax,First
	xor ecx,ecx
;	xor esi,esi
	mov ecx,1
	mov dword[cnt],0
	
pqr:	cmp byte[eax],','
	jz stu
	inc eax
	inc ecx
	jmp pqr
	
stu:	push ecx
;	add dword[cnt],ecx
    ;	xor ecx,ecx
	xor esi,esi
	inc eax
	
again:	cmp byte[eax],','
	push ecx
	jz check
	inc eax
	pop ecx
	inc ecx
	jmp again

check:	pop ecx
	inc ecx
	inc eax
	cmp byte[eax],'m'
	push ecx
	jz final

next:	pop ecx
	add ecx,dword[cnt]
	inc ecx
	push ecx
next1:	cmp byte[eax],10
	jz go
	cmp byte[eax],0
	jz pqr
	inc eax
	pop ecx
	inc ecx
	push ecx
	jmp next1

final:	push eax	
	mov ebx,First
	mov esi,dword[cnt]
	add ebx,esi
	mov dword[cnt],esi
	mov edx,Third
	
ttt:	cmp byte[ebx],','
	jz append
	mov al,byte[ebx]
	mov byte[edx],al
	inc ebx
	inc edx
	jmp ttt

append:	inc edx
	mov byte[edx],' '
	pop eax
	jmp next1

go:	pop ecx
	mov edx,ecx
	mov eax,4
	mov ebx,1
	mov ecx,Third
	int 0x80
	
	mov eax,4
	mov ebx,1
	mov ecx,nl
	mov edx,2
	int 0x80	

end:	add esp,4
	leave	

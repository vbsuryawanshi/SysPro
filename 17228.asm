section .data
	First db '17228,vaibhav,f,msc',0	;20
	      db '17219,ashish,m,msc',0
	      db '17228,vaibhav,m,msc',10,0
	nl db 10,0

section .bss
	Third resb 25

section .text
	global main

main:
	mov eax,First
	xor ecx,ecx
	
pqr:	cmp byte[eax],','
	jz stu
	inc eax
	inc ecx
	jmp pqr
	
stu:	inc ecx	
	push ecx
	xor esi,esi
	inc eax
	
again:	cmp byte[eax],','
	jz check
	inc eax
	inc esi
	jmp again

check:	inc eax
	inc esi
	cmp byte[eax],'m'
	je final

next:;	inc esi
	pop ecx
	add ecx,esi
	push ecx
	push eax
	
next1:	pop eax
	cmp byte[eax],10
	jz go
	cmp byte[eax],0
	jz pqr
	inc eax
	pop ecx
	inc ecx
	push ecx
	push eax
	jmp next1

final:	inc esi	
	pop ecx
	push eax	
	mov ebx,First
	add ebx,ecx
	push ecx
	xor edx,edx
	mov edx,Third
	
ttt:	cmp byte[ebx],','
	jz append
	mov al,byte[ebx]
	mov byte[edx],al
	inc ebx
	inc edx
	pop ecx
	inc ecx
	push ecx
	jmp ttt

append:	inc edx
	mov byte[edx],' '
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

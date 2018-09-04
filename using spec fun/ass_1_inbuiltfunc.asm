section .data
	First db '17228,vaibhav,M,msc',0
	      db '17219,ashish,f,msc',0
	      db '17218,brijesh,M,msc',10,0
	nl db 10,0
	len equ $-First

section .bss
	cnt resd 1
	Result resb len
section .text
	global main
	
main:
	xor edi,edi
	xor ecx,ecx
	xor esi,esi
	
	mov edi,First
	mov ecx,len
loop:	mov al,','
	repne scasb
	mov esi,edi
	mov al,','
	repne scasb
	cmp byte[edi],'M'
	jne go
	mov edx,edi
	push edx
	
	mov dword[cnt],0
	mov dword[cnt],ecx
	sub edi,esi
	mov ecx,edi
	dec ecx

	mov edi,Result
	rep movsb
	
	pop edx
	mov edi,edx
	mov ecx,dword[cnt]
go:	mov al,0
	repne scasb
	push edi
	cmp ecx,0
	je end
	
	mov eax,4
	mov ebx,1
	mov ecx,Result
	int 0x80
	
	mov eax,4
	mov ebx,1
	mov ecx,nl
	mov edx,1
	int 0x80	

	pop edi
	mov ecx,dword[cnt]
	jmp loop
	
end:	add esp,4
	mov eax,4
	mov ebx,1
	mov ecx,Result
	int 0x80

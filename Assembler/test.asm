section .data
	abc dd 10
	def dd 20
	msg db "Addition is %d",10,0
		
section .text
	global main
	extern printf
		
main:
	mov eax,dword[abc]
	mov ebx,dword[def]
	add ecx,dword[def]
	mov eax,ecx
	add eax,ebx
	push eax
	push msg
	call printf
	add esp,8

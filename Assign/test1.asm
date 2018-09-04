section .data
	a dd 10, 20,30,40
	msg db "Add is:%d",10,0
	len equ $-str1

section .text
	global main
	extern printf
1 main:
2	mov eax,dword[a]
3	mov edx,dword[b]
4	add eax,edx
5	push eax
6	push msg
7	call printf
8	add esp,8

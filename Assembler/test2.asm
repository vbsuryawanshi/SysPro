SECTION .data
	msg dq 50,90,87,96,65,1,2,3,6
	string db "Vaibhav%d",10,0
	data1 dd 7,8,9,6,5,4
	First dd 10,20,30,40
	op db "%d",10,0
section .bss
	no1 resd 5
	no2 resq 6
	no3 resd 1
section .text
	extern printf
global main
main:
	mov esi, First
	xor eax,eax
	mov al,0
	xor ecx,ecx
lp:
	cmp byte[esi],0
	jz tst
	inc ecx
	inc esi
	jmp lp	
tst:
	push ecx
	push msg
	call printf
	add esp,8
	add esi,89
	mov eax,op
	push ecx
	push eax
	call printf
	add esp,8

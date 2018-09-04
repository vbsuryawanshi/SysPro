section .data
	First db '17228,vaibhav,m,msc',0
	      db '17227,mayur,m,msc',0
	      db '17119,brijesh,m,mca',0
	      db '17219,ashish,m,msc',0
	      db '17228,vaibhav,m,msc',0
	      db '17119,brijesh,m,mca',0
	      db '17219,ashish,m,msc',10
	len equ $-First
	op db "%d",10,0
	
section .text
	global main
	extern printf
main:
	xor ecx,ecx
	xor edx,edx
	mov edi,First
	mov ecx,len
loop:	mov al,0
	repne scasb
	inc edx
	cmp ecx,0
	jne loop

	push edx
	push op
	call printf
	add esp,8

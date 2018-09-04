section .data
	msg db "Addition is %d",10,0
	msg1 db "Enter the value of n:",0
	acc db "%d",0
section .bss
	n resd 1
	arr resd 100
	ip resd 1
	sum resd 1
;	four resd 1
;	vinc resd 1
section .text
	global main
	extern printf,scanf
1 main:	pusha
2	push msg1
3	call printf
4	add esp,4
5	push n
6	push acc
7	call scanf
8	add esp,8
9	popa	
10	xor ecx,ecx
11	xor esi,esi
12 loop:	mov esi,arr
13	cmp ecx,dword[n]
14	je calculate
15	mov eax,4
16	mul ecx
17	add esi,eax
18	push ecx
19	push esi
20	push acc
21	call scanf
22	add esp,8
23	pop ecx
24	inc ecx
25	jmp loop	
26 calculate:
27	mov ebx,dword[n]
28	xor ecx,ecx
29	xor edi,edi
30 again:	mov esi,arr
31	mov eax,4
32	mul ecx
33	add esi,eax
34	add edi,dword[esi]    			
35	inc ecx
36	dec ebx
37	cmp ebx,0
38	jne again
39 end:	push edi
40	push msg
41	call printf
42	add esp,8

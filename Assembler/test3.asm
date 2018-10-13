section .data
	abc dd 10
	def dd 20
	msg db "Addition is %d",10,0
		
section .text
	global main
	extern printf
		
main:
mov eax,ecx
mov ecx,ecx
mov edx,ecx
mov ebx,ecx
mov esp,ecx
mov ebp,ecx
mov esi,ecx
mov edi,ecx
mov eax,ebx

add eax,ecx
add ecx,ecx
add edx,ecx
add ebx,ecx
add esp,ecx
add ebp,ecx
add esi,ecx
add edi,ecx

mov eax,000
mov ecx,001
mov edx,010
mov ebx,011
mov esp,100
mov ebp,101
mov esi,110
mov edi,111

add eax,000
add ecx,001
add edx,010
add ebx,011
add esp,100
add ebp,101
add esi,110
add edi,111


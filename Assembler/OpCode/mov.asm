	section .data
	a db 9
	section .text
	global main
	
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

mov eax,000
mov ecx,001
mov edx,010
mov ebx,011
mov esp,100
mov ebp,101
mov esi,110
mov edi,111

mov eax,104
mov ecx,104
mov edx,104
mov ebx,104
mov esp,104
mov ebp,104
mov esi,104
mov edi,104
	 
mov eax,dword[a]
mov ecx,dword[a]
mov edx,dword[a]
mov ebx,dword[a]
mov esp,dword[a]
mov ebp,dword[a]
mov esi,dword[a]
mov edi,dword[a]

mov dword[a],eax
mov dword[a],ecx
mov dword[a],edx
mov dword[a],ebx
mov dword[a],esp
mov dword[a],ebp
mov dword[a],esi
mov dword[a],edi

mov eax,dword[eax+ebx*2]
mov ecx,dword[ecx+ebx*2]
mov edx,dword[edx+ebx*2]
mov ebx,dword[ebx+ebx*2]
mov esp,dword[esp+ebx*2]
mov ebp,dword[ebp+ebx*2]
mov esi,dword[esi+ebx*2]
mov edi,dword[edi+ebx*2]

mov dword[a],10

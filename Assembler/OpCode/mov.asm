	section .data
	a db 9
	section .text
	global main
	
main:
mov eax,000
mov ecx,001
mov edx,010
mov ebx,011
mov esp,100
mov ebp,101
mov esi,110
mov edi,111
	 
mov dword[a],ecx

mov eax,ecx
mov ecx,ecx
mov edx,ecx
mov ebx,ecx
mov esp,ecx
mov ebp,ecx
mov esi,ecx
mov edi,ecx


mov eax,3
mov ecx,3
mov edx,3
mov ebx,3
mov esp,3
mov ebp,3
mov esi,3
mov edi,3

mov eax,dword[a]
mov ecx,dword[a]
mov edx,dword[a]
mov ebx,dword[a]
mov esp,dword[a]
mov ebp,dword[a]
mov esi,dword[a]
mov edi,dword[a]

mov dword[a],10
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

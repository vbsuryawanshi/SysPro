	section .data
	a db 9
	section .text
	global main
	
main:
add eax,000
add ecx,001
add edx,010
add ebx,011
add esp,100
add ebp,101
add esi,110
add edi,111
	 
add dword[a],ecx

add eax,ecx
add ecx,ecx
add edx,ecx
add ebx,ecx
add esp,ecx
add ebp,ecx
add esi,ecx
add edi,ecx


add eax,104
add ecx,104
add edx,104
add ebx,104
add esp,104
add ebp,104
add esi,104
add edi,104

add eax,dword[a]
add ecx,dword[a]
add edx,dword[a]
add ebx,dword[a]
add esp,dword[a]
add ebp,dword[a]
add esi,dword[a]
add edi,dword[a]

add dword[a],10
add dword[a],ecx
add dword[a],edx
add dword[a],ebx
add dword[a],esp
add dword[a],ebp
add dword[a],esi
add dword[a],edi

add eax,dword[eax+ebx*2]
add ecx,dword[ecx+ebx*2]
add edx,dword[edx+ebx*2]
add ebx,dword[ebx+ebx*2]
add esp,dword[esp+ebx*2]
add ebp,dword[ebp+ebx*2]
add esi,dword[esi+ebx*2]
add edi,dword[edi+ebx*2]

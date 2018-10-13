	section .data
	a db 9
	section .text
	global main
	
main:
sub eax,ecx
sub ecx,ecx
sub edx,ecx
sub ebx,ecx
sub esp,ecx
sub ebp,ecx
sub esi,ecx
sub edi,ecx

sub eax,000
sub ecx,001
sub edx,010
sub ebx,011
sub esp,100
sub ebp,101
sub esi,110
sub edi,111

sub eax,104
sub ecx,104
sub edx,104
sub ebx,104
sub esp,104
sub ebp,104
sub esi,104
sub edi,104
	 
sub eax,dword[a]
sub ecx,dword[a]
sub edx,dword[a]
sub ebx,dword[a]
sub esp,dword[a]
sub ebp,dword[a]
sub esi,dword[a]
sub edi,dword[a]

sub dword[a],eax
sub dword[a],ecx
sub dword[a],edx
sub dword[a],ebx
sub dword[a],esp
sub dword[a],ebp
sub dword[a],esi
sub dword[a],edi

sub eax,dword[eax+ebx*2]
sub ecx,dword[ecx+ebx*2]
sub edx,dword[edx+ebx*2]
sub ebx,dword[ebx+ebx*2]
sub esp,dword[esp+ebx*2]
sub ebp,dword[ebp+ebx*2]
sub esi,dword[esi+ebx*2]
sub edi,dword[edi+ebx*2]

sub dword[a],10

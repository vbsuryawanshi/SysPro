;;; program is for b^2-4ac

section .data
	b dq 3.0
	a dq 2.0
	c dq 1.0
	
section .bss
	Mfirst resq 1	;reserve quard
	Msnd resq 1
	Four resb 1
	
section .text
	global main
	extern printf

main:
	mov dword[Four],4
	fld qword[b]		;load float in st0
	fmul qword[b]		;multiplication in st0
	fstp qword[Mfirst]
	fld qword[a]
	fmul qword[c]
	fild dword[Four]	;load integer value in float regester
	fmul st1
	fchs 	     ;change the sign of value store in st0
	fadd qword[Mfirst]
	fsqrt

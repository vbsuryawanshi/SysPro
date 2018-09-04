section .data
	First dq 10.0
	Snd dq 20.0
	Third dq 30.0
	Fourth dq 40.0
	msg db "Addition is %f",10,0
section .bss
	Mfirst resq 1	;reserve quard
	Msnd resq 1

section .text
	global main
	extern printf

main:
	fld qword[First]	;load float
	;fadd qword[[Snd]
	fld qword[Snd]
	fadd sto,st1
	fstp qword[Mfirst]	;it stores and pops
	fldz
	fld qword[Mfirst]
	sub esp,8
	fstp qword[esp]
	
	push msg
	call printf
	add esp,12

%macro first 2
	mov eax,%1	;%1 denote 1st position of parameter i.e 10
%%lp:	mov ebx,%2
	add eax,ebx
%endmacro
section .text
	global main
	
main:
	first 10,20
	first 30,50

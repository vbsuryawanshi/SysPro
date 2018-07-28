section .data
	first db 'ABCD EFGH IJKL MNOP'
	second db 'HGFE DCBA'

	global main
	extern puts
main:	push first
	call puts
	add esp,4

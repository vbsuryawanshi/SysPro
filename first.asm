section .data
	first db 'ABCD EFGH'10,0
	second dd 45
	third dq 4.94
section .text
	global main
main: ret

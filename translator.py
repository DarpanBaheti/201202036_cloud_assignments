#

#reading 32bit file
f = open("file_32bit.asm",'r')
#writing to output file
f2 = open("output_64bit.asm","w")
"""
converting 32bit file to 64bit file
by converting each line
"""
ctr = 1
f2.write("extern printf\n")
for line in f:
	if line=="_start:\n":
        	f2.write(line)
        	f2.write("push rbp\n")
    	elif line=="global  _start\n":
        	f2.write("global  _start\n")
    	elif line=="mov edx,len\n":
        	f2.write("mov rdi,fmt\n")
    	elif line=="section .data\n":
        	f2.write("section .data\n")
    	elif line=="section .text\n":
        	f2.write("section .text\n")
    	elif line=="mov ecx,msg\n":
        	f2.write("mov rsi,msg\n")
    	elif line=="mov ebx,1\n":
        	f2.write("mov rax,0\n")
    	elif line=="int 0x80\n" and ctr==1:
        	f2.write("call printf\n")
        	f2.write("pop rbp\n")
        	ctr=2
    	elif line=="int 0x80\n" and ctr==2:
        	f2.write("ret\n")
    	elif line=="mov ebx,0\n":
        	f2.write("mov rax,0\n")
    	elif line=="len equ $ - msg\n":
        	f2.write("fmt:  db \"%s\", 10, 0\n")
    	elif line=="msg db \"Hello world !!!\",0xa\n":
        	f2.write("msg:  db \"Hello world !!!\", 0\n")


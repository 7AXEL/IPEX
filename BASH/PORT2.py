#IMPORTS
from termcolor import colored as c 
from INDEX import INDEX as i
from time import sleep as  s
import socket as z 
import os
#VARIABLES
u = f"""\r{i.purple}┌─[AXEL@OPTION]─[~]
{i.purple}└──❯❯❯"""
o = '༆'
n = 1
h = '      '
p = ""*10
b ='='
y = '>'
#TITLE
os.system('python TITLE.py')
#RUN
print(c("____________________________________",'red'))
while n <= 10 :
        	print(c(f"\r{o}PROGRESS➺{n*10}%{o}{h}{i.green}\t{b*n}{y}",'yellow')+p,end="")
        	s(0.1)
        	n += 1
print(f"{h}")
print(c(f"☬☞STARTED{h}",'green'))
try:
	while True :
		port = input(u)
		print(c(f"{z.getservbyname(port)}",'red'))
except:
		print(c(f"➺ENTER VALIDE OPTION{h}",'blue'))
		s(2)
		os.system('clear')
		os.system('python PORT2.py')
			





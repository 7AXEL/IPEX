#IMPORTS
from termcolor import colored as c
from INDEX import INDEX as i
from time import sleep as s
import os
#VARIABLES
u = f"""{i.green}┌─[IPEX@OPTION]─[#] 
{i.green}└──❯❯❯"""
o = '༆'
n = int(1)
h = '      '
p = ""*10
b= '='
y = '>'
k = int(1)
#TITLE
os.system('clear')
os.system('python TITLE.py')
#RUN
print(c("____________________________________",'red'))
while n <= 10 :
        	print(c(f"\r{o}PROGRESS➺{n*10}%{o}{h}{i.green}\t{b*n}{y}",'yellow')+p,end="")
        	s(0.1)
        	n += 1
def menu():
        	print(f"{h}")
        	print(f"{i.yellow}[1]{i.cyan}IP-GPS SCRAPER")
        	print(f"{i.yellow}[2]{i.cyan}IP-HOST SCRAPER")
        	print(f"{i.yellow}[3]{i.cyan}IP-PORT SCRAPER")
        	print(f"{i.yellow}[4]{i.cyan}IP-LOCAL HOST SERVER")
        	print(f"{i.yellow}[5]{i.purple}IPEX-ABOUT")
        	print(f"{i.yellow}[×]{i.red}IPEX-EXIT")
menu()
option = input(u)
if option == '1' :
	os.system('bash GPS.sh')
elif option == '2' :
        	os.system('bash HOST.sh')
elif option == '3' :
        	os.system('bash PORT.sh')
elif option == '4' :
        	os.system('bash SERVER.sh')
elif option == '5' :
        	os.system('python ABOUT.py')

   	
   	


        	

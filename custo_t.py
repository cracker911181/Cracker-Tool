# Coded by Cracker 
# CRACKER911181
 


import os,time,sys
colouroff="\x1b[00m"
red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Termux Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Set Termux Banner\n\t\t2.Change Background Color\n\t\t3.Change Font"+red+"\n\t\t00.Back To HOME\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		
		oo=open('banr_t.py',"r").read()
		os.system("clear")
		exec(oo)
		
	elif chose=="2":
		oo=open("colr_t.py","r").read()
		os.system("clear")
		exec(oo)
	
	elif chose=="3":
		oo=open("fnt_t.py","r").read()
		os.system("clear")
		exec(oo)
		
	elif chose=="00":
		break
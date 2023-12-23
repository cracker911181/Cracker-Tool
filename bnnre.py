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


def make():
	print(blue+"\n\tThis Tool Needed Storage Permission")
	os.system('termux-setup-storage')
	print(pest+"\n\t\tDONE")
	print(pest+"\n\tBanner Setup On Termux")
	nm=str(input(rosy+"\nEnter Your Name: "))
	print(pest+"\n\tSet Your Password")
	pd=str(input(rosy+"\nEnter Your Password: "))
	pd1=str(input("Confirm Your Password: "))
	os.system("rm -rf /data/data/com.termux/files/usr/etc/motd")
	oo=open("/data/data/com.termux/files/usr/etc/bnnr.py","w")
	if pd==pd1:
		print(green+"")
		print()
		print(pest+"Banner Set & User Termux Is Now Password Protected")
		time.sleep(2)
		a="""
def ban():
	import os,time,sys
	red="\x1b[91m"
	green="\x1b[92m"
	rosy="\x1b[95m"
	pest="\x1b[96m" #pest

	pas='"""+pd+"""'

	while True:
		os.system('clear')
		print(green+"")
		os.system('figlet """+nm+"""')
		print(pest+'			developed by cracker911181')
		pwd=str(input(rosy+"Enter Your Password: "))
		if pas==pwd:
			print()
			print(green+"	Login Successfull")
			time.sleep(1.5)
			os.system('clear')
			print(green+"")
			os.system('figlet """+nm+"""')
			print(pest+'			developed by cracker911181')
			break 
			sys.exit()
		else:
			print()
			print()
			print(red+"	Password Not Match")
			time.sleep(1.5)
try:
	ban()
except:
	ban()"""


		oo.write(a)
		oo1=open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
		oo1.write("PS1='$ '\npython /data/data/com.termux/files/usr/etc/bnnr.py \ncd $HOME")
	else:
		print(red+"")
		print()
		print("	Password Not Match")
		time.sleep(3)

while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Termux Banner [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Set Termux Banner"+red+"\n\t\t00.Back To HOME\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		try:
			make()
		except:
			make()
	
	elif chose=="00":
		break

# Coded by Cracker 
# CRACKER911181 

# last

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
	from cracker_say import bennar
	red="\x1b[91m"
	green="\x1b[92m"
	rosy="\x1b[95m"
	pest="\x1b[96m" #pest

	pas='"""+pd+"""'

	while True:
		os.system('clear')
		print(green+"")
		
		colouroff="\x1b[00m" 
		red1="\x1b[41m" #red1

		os.system("python /data/data/com.termux/files/usr/etc/andro.py")
		
		print()
		
		print()
		pwd=str(input(rosy+"Enter Your Password: "))
		if pas==pwd:
			print()
			print(green+"	Login Successfull")
			time.sleep(1.2)
			os.system('clear')
			print(colouroff+"")
			bennar('"""+nm+"""')
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
		os.system("mv andro.py /data/data/com.termux/files/usr/etc")
	else:
		print(red+"")
		print()
		print("	Password Not Match")
		time.sleep(3)
	

try:
	make()
except:
	make()

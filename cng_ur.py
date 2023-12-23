# Coded by Cracker 
# CRACKER911181
 

import os,time,sys



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

def hide():

	vicurl=str(input(rosy+"\n\nEnter Your URL: "))
	doman=str(input("Enter A Domain (eg: 'https://google.com'): "))

	print(pest+"\n\n\t\tGenarating Your Link\n")

	os.system("curl -s https://is.gd/create.php\?format\=simple\&url\="+vicurl+" >> ln.test")
	oo=open("ln.test","r").read()

	oo1=oo.find("://")
	ox=str(oo[oo1+3:])
	real=str(yellow+"\n\nYour Link:	"+doman+"-@"+ox)

	print(real)
	os.system("rm ln.test")
	time.sleep(7)


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] URL Changer [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Change URL\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		hide()
	elif chose=="00":
		break

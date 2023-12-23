
# Coded by Cracker
# CRACKER911181
 

import os


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

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
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t       """+blue+"""[★] Subdomain Scanner [★] \n"""+green+""" ========================================================="""+colouroff)
	chose=str(input(pest+"\n\n\t\t1.Subdomain Scanner\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	if chose=="1":
		
		os.system("python sbd.py")
	
	elif chose=="00":
		break
# Coded by Cracker
# CRACKER911181
 

grn="\x1b[92m" 
blu="\x1b[94m" 

import base64, os
print(blu+"\n\n[+]This Tool Needed Storage Permission\n")
os.system('termux-setup-storage')
print(grn+"\n\n\tPermission Goted")
import time, sys



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
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t       """+blue+"""[★] Python Obfuscate [★] \n"""+green+""" ========================================================="""+colouroff)
	chose=str(input(pest+"\n\n\t\t1.Python Script Obfuscate\n\t\t"+red+"00.Back To HOME\n\n"+rosy+"Enter Your Option: "))
	if chose=="1":
	
		file=str(input(rosy+"\n\nEnter Your Python File Full Path: "))
		os.system("python pluso.py "+file+" '*'")
		ox=(file.replace(".py","enc.py"))
		try:
			open(file,"r")
			print(pest+"\n\tFile Encode Done\n")
			path=str(input(rosy+"Enter Your File Saving Path: "))
			flx=str(input(rosy+"Enter Your Saving File Name: "))
			file1=str(path+"/"+flx)
			os.system("mv "+ox+" "+ file1)
			print(pest+"\n\nFile Saved On "+file1)
			
		
		except FileNotFoundError:
			print(red+"\n\tYou Entered File Path is Not Dinied")
		
		time.sleep(3)
	
	
	
	
	elif chose=="00":
		break

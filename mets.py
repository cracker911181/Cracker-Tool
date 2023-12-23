
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


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t        """+blue+"""[★] Termux Framework [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Install Metasploit\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		os.system("chmod +x meta.sh")
		os.system("./meta.sh")
		os.system("chmod +x postgresql_ctl.sh")
		os.system("./postgresql_ctl.sh start")
		os.system("clear")
		print("\n\n\n\n\n\t     "+yellow+"Metasploit Installing Done\n\n\t"+green+"To Run Metasploit Type 'msfconsole' ")
		time.sleep(7)
	

		
	elif chose=="00":
		break
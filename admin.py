# Coded by Cracker
# CRACKER911181


import os,time,sys
#text colour()
#creator: CRACKER911181
colouroff="\x1b[00m"
white = '\33[00m'
red = '\33[91m'
green = '\33[92m'
yellow = '\33[93m'
blue = '\33[94m'
rosy = '\33[95m'
pest = '\33[96m'

while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Admin Finder [★] \n"""+green+""" ========================================================="""+colouroff)
  
	chose=str(input(pest+"\n\n\t\t1.Admin Finder\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		os.system("python adm.py")
	elif chose=="00":
		break
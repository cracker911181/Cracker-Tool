# Coded by Cracker
# CRACKER911181
 

import time,os,sys

#text colour()
#creator: CRACKER911181

colouroff = '\33[00m'
off="\x1b[00m"
un="\x1b[4m"
white = '\33[00m'
red = '\33[91m'
green = '\33[92m'
yollow = '\33[93m'
blue = '\33[94m'
rosy = '\33[95m'
pest = '\33[96m'
#colour end

def lg():
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""           6 Crack Your World, If You Can\n\n\t           """+blue+"""[★] BD Cloning [★] \n"""+green+""" ========================================================="""+colouroff)
for i in range(1000):
	os.system('clear')
	lg()
	chose=str(input(pest+"\n\n\t\t 1.BD FB Cloning\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		os.system("clear#")
		print(green+"\n\n\t\t   Choose Your Code >>"+pest+"\n\n\t\t171, 172, 178, 170, 130\n\t\t170, 177, 179, 131, 181\n\t\t132, 173, 175, 191, 192\n\t\t193, 194, 195, 196, 151\n\t\t152, 153, 154, 155, 156\n\t\t157, 183, 184, 185, 186\n\t\t191, 192, 197, 198, 199")
		code=str(input(rosy+"\nEnter Your Code: "))

		os.system('clear')

		print(blue+"""
|=========================|
|     Cracking Start      |
|+++++++++++++++++++++++++|
| Country    :     BD     |   """+white+un+"""https://t.me/cracker911181"""+off+blue+"""
| Time       : """,time.strftime("%I:%M:%S"),""" |
| Limit      :   9999999  |        """+white+un+"""@cracker911181"""+off+blue+"""
|=========================|
""")
		print(red+"\n\t      To Exit: Pess (Ctrl +c)\n")
		oo=open("cln.py","r")
		
		exec(oo.read())

	elif chose=="00":
		break
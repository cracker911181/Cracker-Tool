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

def color():
	
	print(pest+"""
	1.FiraCode
	2.Source-Code-Pro
	3.Go
	4.Fantasque
	5.Iosevka
	6.OpenDyslexic
	7.Hermit
	8.Inconsolata
	9.Monofur
	10.Meslo
	11.DejaVu
	12.Monoid
	13.Hack
	14.Roboto
	15.Ubuntu
	16.Courier-Prime
	17.LiberationMono
	18.Fira
	19.Anonymous-Pro
	20.GNU-FreeFont
       """+green+"""	21.Reset Fonts""")
	
	chose=str(input(rosy+"\n\nEnter Your Color: "))
	
	
	if chose=="21":
		os.system("rm -rf /data/data/com.termux/files/home/.termux/font.ttf")
			
	else:

		open("/data/data/com.termux/files/home/Cracker-Tool/.ctermux/font/"+chose+".ttf","r")
		os.system("cp /data/data/com.termux/files/home/Cracker-Tool/.ctermux/font/"+chose+".ttf /data/data/com.termux/files/home/.termux")
		os.system("mv /data/data/com.termux/files/home/.termux/"+chose+".ttf /data/data/com.termux/files/home/.termux/font.ttf")


while True:
	os.system("clear")
	try:
		color()
		print(yellow+"\n\n\t\tDone")
		time.sleep(5)
		break
	except FileNotFoundError:
		
		print(red+"\n\n\tInvalid Color Number")
		time.sleep(2)
		
		pass
	except PermissionError:
		pass
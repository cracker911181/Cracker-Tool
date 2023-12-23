
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



def dot(user):
	lnusr=len(user)
	
	dot=open("/data/data/com.termux/files/home/Cracker-Tool/.test/dlist.txt","r").read()
	spdot=dot.split("\n")
	x=1
	
	for new in spdot:
		for next in range(lnusr):
			main1=((user[:x])+"."+(user[x:]))
		
			per=str(main1+new)
			print(per)
		
			if x==lnusr-1:
				x=1
			else:
				x=x+1

def main1():
	us=str(input(rosy+"Enter Your Gmail: "))
	user=us.split("@")
	print(yellow+"\n\n\t\tYour Genarated Gmail List\n\n"+pest)
	time.sleep(1)
	dot(user[0])

def main():
	main1()
	input(blue+"\n\n        Press Enter To Back Previous Menu ")

while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t        """+blue+"""[★] GMAIL Genarator [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Gmail Genarate(Dot & Plus Trick)\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	if chose=="1":
		os.system("clear")
		main()
		
	elif chose=="00":
		break

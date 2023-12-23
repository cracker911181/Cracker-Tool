# Coded by Cracker
# CRACKER911181
 

import os,time,sys

from bs4 import BeautifulSoup



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

print(green+"")
os.system("figlet SqL - Tool")
time.sleep(.5)
os.system("chmod +x *")
try:
	os.system("./temp.sh")
	os.system("rm -rf temp.sh")
except:
	pass


while True:
	os.system("clear")
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] SQL Injection [★] \n"""+green+""" ========================================================="""+colouroff)
	choose=str(input(pest+"\n\n\t\t1.SQL-Injection\n\t\t2.Link Extractor\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	if choose=="1":
		os.system("./.mn.sh")
	elif choose=="00":
		break
	elif choose=="2":
		
		url=str(input(rosy+"\n\nEnter Target URL: "))
		try:
			import requests
			reqs = requests.get(url)
			print("\n\n")
			soup = BeautifulSoup(reqs.text, 'html.parser')
			for ink in soup.find_all('a'):
				link=(ink.get('href'))
				if link=="#main":
					continue
				else:
					print(green+link)
			time.sleep(7)
			
		except requests.exceptions.MissingSchema:
			print(red+"\n\n       ❌Link Not Valid❌    ")
			time.sleep(2)
		

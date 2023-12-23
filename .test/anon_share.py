# Coded by Cracker
# CRACKER911181



import requests
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



def anon_share(file_name,path):
	
	files= {'file': (file_name, open(path, 'rb'))}
	
	data = requests.post("https://api.anonfiles.com/upload", files=files).json()
	
	
	print(yellow+"\n\nLong URL: "+str(data["data"]["file"]["url"]["full"])+"\nShort URL: "+str(data["data"]["file"]["url"]["short"]))
	


def main():
	os.system("clear")
	print(blue+"\n\n              Share Your File Anonymously")
	path=str(input(rosy+"\n\nEnter Your File Location: "))
	
	file=str(input(rosy+"\nEnter Your File Name: "))
	
	print(green+"\n\n\n                    Please Wait...")
	anon_share(file,path)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")



def mainner():
	try:	
		main()
	except requests.exceptions.SSLError:
		print(red+"\n\n\n                Turn ON VPN and Try Again!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except FileNotFoundError:
		print(red+"\n\n\n\n                   File Not Found!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\n\n             Check Your Internet Connection!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	
	except:
		print(red+"\n\n\n\n                  Something Went Wrong!!") 
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	
	



while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Anon Share [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Share File Anonymously\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		mainner()
		
	elif chose=="00":
		break
		
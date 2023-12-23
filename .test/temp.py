
# Coded by Cracker
# CRACKER911181
 

import requests
import random
import string
import time
import sys
import re
import os




userlist=[]
listid=[]



name=string.ascii_lowercase + string.digits
for x in range(10):
	user=''.join(random.choice(name))
	userlist.append(user)

username=((''.join(userlist)))
mail=(username+"@1secmail.com")

##############################

def create_mail():
	
	requests.get("https://www.1secmail.com/api/v1/?login="+username+"&domain=1secmail.com")
	os.system("clear")
	print("\x1b[96m\n\tYour Mail is: \x1b[93m"+mail+"\x1b[95m\n\n\t  To Stop Temp Mail Press \x1b[91mCtrl + c\x1b[00m")


def ckmail():
	mail_list=requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+username+"&domain=1secmail.com").json()

	

	if len(mail_list)==0:
		
		pass
	else:
		mail_lists=(mail_list[0])
		for new,now in mail_lists.items():
			

			if new=="id":
				if now in listid:
					pass
				else:
					msgread=requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+username+"&domain=1secmail.com&id="+str(now)).json()
				
					
					
					for k,v in msgread.items():
						if k == 'from':
							sender = v
						if k == 'subject':
							subject = v
						if k == 'date':
							date = v
						if k == 'textBody':
							content = v
							
					print("\x1b[92m\n\n\t    A New Mail Found\n\x1b[00m\nSender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')
					print("\x1b[91m\n\n========================================================\n\x1b[00m")
					listid.append(now)
				
def mainner():
	create_mail()
	while True:
		#makeusr()
		try:
			ckmail()
		except(KeyboardInterrupt):
			input("\n\n\t\x1b[94mPress Enter To Back Previous Menu: ")
			break

	
def main():
	try:
		mainner()
	
	except requests.exceptions.ConnectionError:
		print("\n\n\t\x1b[91mPlease Check Your Internet Connection")
		time.sleep(5)
	except:
		print("\n\n\t\x1b[91m    Someting went  Wrong!")
		time.sleep(5)



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
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Temp Mail [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Temp Mail\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	if chose=="1":
		main()
	elif chose=="00":
		break

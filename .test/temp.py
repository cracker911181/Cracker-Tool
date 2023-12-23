
# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD
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
=======
import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCByYW5kb20KaW1wb3J0IHN0cmluZwppbXBvcnQgdGltZQppbXBvcnQgc3lzCmltcG9ydCByZQppbXBvcnQgb3MKCgoKCnVzZXJsaXN0PVtdCmxpc3RpZD1bXQoKCgpuYW1lPXN0cmluZy5hc2NpaV9sb3dlcmNhc2UgKyBzdHJpbmcuZGlnaXRzCmZvciB4IGluIHJhbmdlKDEwKToKCXVzZXI9Jycuam9pbihyYW5kb20uY2hvaWNlKG5hbWUpKQoJdXNlcmxpc3QuYXBwZW5kKHVzZXIpCgp1c2VybmFtZT0oKCcnLmpvaW4odXNlcmxpc3QpKSkKbWFpbD0odXNlcm5hbWUrIkAxc2VjbWFpbC5jb20iKQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgpkZWYgY3JlYXRlX21haWwoKToKCQoJcmVxdWVzdHMuZ2V0KCJodHRwczovL3d3dy4xc2VjbWFpbC5jb20vYXBpL3YxLz9sb2dpbj0iK3VzZXJuYW1lKyImZG9tYWluPTFzZWNtYWlsLmNvbSIpCglvcy5zeXN0ZW0oImNsZWFyIikKCXByaW50KCJceDFiWzk2bVxuXHRZb3VyIE1haWwgaXM6IFx4MWJbOTNtIittYWlsKyJceDFiWzk1bVxuXG5cdCAgVG8gU3RvcCBUZW1wIE1haWwgUHJlc3MgXHgxYls5MW1DdHJsICsgY1x4MWJbMDBtIikKCgpkZWYgY2ttYWlsKCk6CgltYWlsX2xpc3Q9cmVxdWVzdHMuZ2V0KCJodHRwczovL3d3dy4xc2VjbWFpbC5jb20vYXBpL3YxLz9hY3Rpb249Z2V0TWVzc2FnZXMmbG9naW49Iit1c2VybmFtZSsiJmRvbWFpbj0xc2VjbWFpbC5jb20iKS5qc29uKCk'
love = 'XPtxXPtycMvOfMJ4boJScoS9fnKA0XG09ZQbXPDxXPDyjLKAmPtyyoUAyBtbWPJ1unJksoTymqUZ9XT1unJksoTymqSfjKFxXPDyzo3VtozI3YT5iqlOcovOgLJyfK2kcp3EmYzy0MJ1mXPx6PtxWPDbXPDxWnJLtozI3CG0vnJDvBtbWPDxWnJLtoz93VTyhVTkcp3EcMQbXPDxWPDyjLKAmPtxWPDyyoUAyBtbWPDxWPJ1mM3WyLJD9pzIkqJImqUZhM2I0XPWbqUEjpmbiY3q3ql4kp2IwoJScoP5wo20iLKOcY3LkYm9uL3Eco249pzIuMR1yp3AuM2HzoT9anJ49Vvg1p2IlozSgMFfvWzEioJScow0kp2IwoJScoP5wo20znJD9VvgmqUVboz93XFxhnaAiovtcPtxWPDxXPDxWPDxXPDxWPDxXPDxWPDyzo3Vtnlk2VTyhVT1mM3WyLJDhnKEyoKZbXGbXPDxWPDxWnJLtnlN9CFNaMaWioFp6PtxWPDxWPDymMJ5xMKVtCFO2PtxWPDxWPJyzVTftCG0tW3A1LzcyL3DaBtbWPDxWPDxWp3IvnzIwqPN9VULXPDxWPDxWnJLtnlN9CFNaMTS0MFp6PtxWPDxWPDyxLKEyVQ0tqtbWPDxWPDycMvOeVQ09VPq0MKu0Dz9xrFp6PtxWPDxWPDywo250MJ50VQ0tqtbWPDxWPDxWPtxWPDxWpUWcoaDbVyk4ZJWoBGWgKT5poyk0VPNtVRRtGzI3VR1unJjtEz91ozEpoyk4ZJWoZQOgKT5GMJ5xMKV6VPVtXlOmMJ5xMKVtXlNaKT4aVPftVyEiBvNvVPftoJScoPNeVPqpovptXlNvH3IvnzIwqQbtVvNeVUA1LzcyL3DtXlNaKT4aVPftVxEuqTH6VPVtXlOxLKEyVPftW1khWlNeVPWQo250MJ50BvNvVPftL29hqT'
god = 'VudCArICdcbicpCgkJCQkJcHJpbnQoIlx4MWJbOTFtXG5cbj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG5ceDFiWzAwbSIpCgkJCQkJbGlzdGlkLmFwcGVuZChub3cpCgkJCQkKZGVmIG1haW5uZXIoKToKCWNyZWF0ZV9tYWlsKCkKCXdoaWxlIFRydWU6CgkJI21ha2V1c3IoKQoJCXRyeToKCQkJY2ttYWlsKCkKCQlleGNlcHQoS2V5Ym9hcmRJbnRlcnJ1cHQpOgoJCQlpbnB1dCgiXG5cblx0XHgxYls5NG1QcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnU6ICIpCgkJCWJyZWFrCgoJCmRlZiBtYWluKCk6Cgl0cnk6CgkJbWFpbm5lcigpCgkKCWV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoKCQlwcmludCgiXG5cblx0XHgxYls5MW1QbGVhc2UgQ2hlY2sgWW91ciBJbnRlcm5ldCBDb25uZWN0aW9uIikKCQl0aW1lLnNsZWVwKDUpCglleGNlcHQ6CgkJcHJpbnQoIlxuXG5cdFx4MWJbOTFtICAgIFNvbWV0aW5nIHdlbnQgIFdyb25nISIpCgkJdGltZS5zbGVlcCg1KQoKCgpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKd2hpb'
destiny = 'THtIUW1MGbXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tITIgpPOALJyfVSivzVIqVSkhVvVvX2qlMJIhXlVvVvN9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0vVvVeL29fo3Ilo2MzXDbWPtbWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKUEpqQRhVSEyoKNtGJScoSkhKUEpqPVepzIxXlVjZP4tDzSwnlOHolOVo21yVvglo3A5XlWpoykhEJ50MKVtJJ91pvOCpUEco246VPVcXDbWPtycMvOwnT9mMG09VwRvBtbWPJ1unJ4bXDbWMJkcMvOwnT9mMG09VwNjVwbXPDyvpzIunj=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

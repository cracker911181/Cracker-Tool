# Coded by Cracker
# CRACKER911181




import requests,json,os,time


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest




def fake_ident():
	data=requests.get("https://randomuser.me/api").json()
	
	
	fname=str(data["results"][0]["name"]["first"]
	)
	lname=str(data["results"][0]["name"]["last"])
	gender=str(data["results"][0]["gender"])
	location=str(str(data["results"][0]["location"]["street"]["number"])+","+str(data["results"][0]["location"]["street"]["name"])+","+str(data["results"][0]["location"]["city"])+","+str(data["results"][0]["location"]["state"])+","+str(data["results"][0]["location"]["country"]))
	postcode=str(data["results"][0]["location"]["postcode"])
	email=str(data["results"][0]["email"])
	user=str(data["results"][0]["login"]["username"])
	pwd=str(data["results"][0]["login"]["password"])
	age=str(data["results"][0]["dob"]["age"])
	pic=str(data["results"][0]["picture"]["large"])
	
	os.system("clear")
	main=(green+"\n\nFirst Name: "+fname+"\nLast Name: "+lname+"\nGender: "+gender+"\nAge: "+age+"\nPicture: "+pic+"\nEmail: "+email+"\nUsername: "+user+"\nPassword: "+pwd+"\nPost Code: "+postcode+"\nLocation: "+location)
	
	print(main)



while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t    """+blue+"""[★] Fake Identity Generator [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Identity Generate\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	
	if chose=="00":
		break

	elif chose=="1":
		fake_ident()
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
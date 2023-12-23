#Developed By CRACKER911181
# Coded By Cracker911181

import os,time,random,requests

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

def ccGen():
	totaldigits=16
	
	inputcvc = int (input(rosy+"\n\nEnter Bin : "))
	totalcc = int (input(rosy+"Number of CC : "))
	lapart = str (inputcvc)
	if len(lapart)==0:
		count = 16
	count = len (str (inputcvc))
	totalbin =  int (count)
	genbin = totaldigits-totalbin
	firstnum =  "1"*genbin
	lastnum = "9"*genbin
	binf =  int (firstnum)
	binl = int (lastnum)
	b = 0
	print("\n\n")
	for i in range (totalcc):
		rancc=str(random.randint(binf,binl))
		cc=lapart+rancc
		ranmonth = str (random.randint (1,12))
		smon =str (ranmonth)
		if len(smon)==1:
			month = "0"+smon
			b = month
		else  :
			month =smon
			b = month
		ranyear = str (random.randint(2022,2025))
		cvc = str (random.randint(111,999))
		validcc=cc+"|"+month+"|"+ranyear+"|"+cvc
		
		print(yellow+"\t"+validcc)
		





def ccck():
	
	cc=str(input(rosy+"\n\nEnter a CC For Check: "))
	if int(cc[0])<4 or int(cc[0])>6:
		print(red+"\n\n\n\t\tYou Entered a Invalid CC!!")
	
	else:
	
		appi=requests.get("https://lookup.binlist.net/"+cc).json()
#	print(appi)
#	except json.decoder.JSONDecodeError:
		
		
	
		schema=str(appi["scheme"])
		type=str(appi["type"])
		try:
			brand=str(appi["brand"])
		except:
			brand="Unknown"
	
		cntry=(appi["country"])
		cname=str(cntry["name"])
		cemoji=str(cntry["emoji"])
		c_curncy=str(cntry["currency"])
		namric=str(cntry["numeric"])
		alpha2=str(cntry["alpha2"])
		clati=str(cntry["latitude"])
		clong=str(cntry["longitude"])
	
		try:
			bnk=(appi["bank"])
		
			try:
				bname=str(bnk["name"])
			except:
				bname="Unknown"
			
			try:
				burl=str(bnk["url"])
			except:
				burl="Unknown"
		
			try:
				bphn=str(bnk['phone'])
			except:
				bphn="Unknown"
		
			try:
				bcity=str(bnk['city'])
			except:
				bcity="Unknown"
			
		except:
			bname="Unknown"
			burl="Unknown"
			bphn="Unknown"
			bcity="Unknown"
		
		main=str(yellow+"\n\nCC → "+cc+" \n\n|\n| Scheme: "+schema+"\n| Type:   "+type+"\n| Brand:  "+brand+"\n|\n| Country |\n          | Name:      "+cname+"\n          | Emoji:     "+cemoji+"\n          | Currency:  "+c_curncy+"\n          | Numeric:   "+namric+"\n          | Alpha2:    "+alpha2+"\n          | Latitude:  "+clati+"\n          | Longitude: "+clong+"\n\n|\n| Bank |\n       | Name:  "+bname+"\n       | URL:   "+burl+"\n       | Phone: "+bphn+"\n       | City:  "+bcity)
		print(main)
		







while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Anon Share [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Check Cradit Card Number(CC)\n\t\t2.Genarate Random CC\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		os.system("clear")
		try:
			ccck()
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		except requests.exceptions.ConnectionError:
			print(red+"\n\n\t   Check Your Internet Connection!!")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
		except:
			print(red+"\n\n\t\tSomething Went Worng!!")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
			
	elif chose=="2":
		os.system("clear")
		try:
			ccGen()
		except:
			print(red+"\n\n\t\tSomething Went Worng!!")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	elif chose=="00":
		break
	
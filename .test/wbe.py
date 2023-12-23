
# Coded by Cracker
# CRACKER911181
 



import requests,socket
import os,sys,time



#text colour()
#creator: CRACKER911181

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



def dns_er():
	domain=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	link=str("http://api.hackertarget.com/dnslookup/?q="+domain)
	dns=requests.get(link).text
	os.system('clear')
	print("\n\n\t    "+green+"Your DNS Result\n\n"+yellow+dns)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")

def dns():
	try:
		dns_er()
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


##########################

def hostsearcher():
	domain=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	link=str("https://api.hackertarget.com/hostsearch/?q="+domain)
	dns=requests.get(link).text
	os.system('clear')
	print("\n\n\t    "+green+"Your HOST FINDER Result\n\n"+yellow+dns)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")
	

def httpfind():
	try:
		hostsearcher()
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


############################

def httpheader():
	domain=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	link=str("https://api.hackertarget.com/httpheaders/?q="+domain)
	dns=requests.get(link).text
	os.system('clear')
	print("\n\n\t    "+green+"Your HTTP HEADER Result\n\n"+yellow+dns)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")


def httphead():
	try:
		httpheader()
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
#############################


def extractor():
	web=str(input(rosy+"\nEnter Your Link without 'https' or 'http': "))
	try:
		data=requests.get("https://api.hackertarget.com/pagelinks/?q="+web).text
		os.system('clear')
		print("\n\n\t    "+green+"Your Extract Link Result\n\n"+yellow+data)
	
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


#############################


def shared_d():
	web=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	try:
		data=requests.get("https://api.hackertarget.com/findshareddns/?q="+web).text
		os.system('clear')
		print("\n\n\t    "+green+"Your Shared DNS Result\n\n"+yellow+data)
	
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


#############################



def open_port():
	web=str(input(rosy+"\nEnter Your IP (eg: '11.11.123.456'): "))
	try:
		data=requests.get("https://internetdb.shodan.io/"+web).json()
		os.system('clear')
		try:
			print("\n\n\t    "+green+"Your Open Port Scanned Result\n\n"+yellow+"Cpes: "+str(data["cpes"])+"\nHostname: "+str(data["hostnames"])+"\nIP: "+str(data["ip"])+"\nPort: "+str(data["ports"])+"\nTags: "+str(data["tags"])+"\nVuln: "+str(data['vulns']))
		except:
			print("\n\n\t    "+green+"Your Open Port Scanned Result\n\n"+yellow+str(data["detail"]))
	
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


#############################








while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] WEB Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.DNS Lookup\n\t\t2.HOST Finder\n\t\t3.HTTP header\n\t\t4.Open Port Scanner\n\t\t5.Shared DNS Finder\n\t\t6.Link Extractor\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		dns()
	
	elif chose=="2":
		httpfind()
	
	elif chose=="3":
		httphead()
	
	elif chose=="4":
		open_port()
	
	elif chose=="5":
		shared_d()
	
	elif chose=="6":
		extractor()
		
	elif chose=="00":
		break



# https://api.hackertarget.com/hostsearch/?q=google.com


# https://api.hackertarget.com/httpheaders/?q=google.com

# https://api.hackertarget.com/zonetransfer/?q=google.com

### link extracktor
# https://api.hackertarget.com/pagelinks/?q=google.com

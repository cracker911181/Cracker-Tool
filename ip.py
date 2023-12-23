import requests
import socket
import time,os,sys


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest




def ipt(ipp=""):
	try:
		api=requests.get("http://ip-api.com/json/"+ipp).json()
	
		tip=str(api["query"])
		status=str(api["status"])
		cntry=str(api["country"])
		cntrycd=str(api["countryCode"])
		region=str(api["region"])
		regionnam=str(api["regionName"])
		city=str(api["city"])
		zip=str(api["zip"])
		lat=str(api["lat"])
		lon=str(api["lon"])
		timezone=str(api["timezone"])
		isp=str(api["isp"])
		org=str(api["org"])
		ass=str(api["as"])
		map=str("https://www.google.com/maps/place/"+str(lat)+"+"+str(lon))
		#map=str(r(lat+"+"+lon))
		main=str("| IP:  "+tip+" \n| Status: "+status+"\n| country: "+cntry+"\n| Country Code: "+cntrycd+"\n| Region: "+region+"\n| Region Name: "+regionnam+"\n| City: "+city+"\n| ZIP: "+zip+"\n| Lat: "+lat+"\n| Lon: "+lon+"\n| Timezone: "+timezone+"\n| ISP: "+isp+"\n| Org: "+org+"\n| AS: "+ass+" \n| Map: "+map)
		print(main)
	
	except:
		pass
	
	input(blue+"\n\n       Press Enter To Back Previous Menu ")


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t           """+blue+"""[★] IP Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Track Your Own IP\n\t\t2. Track Your Victim IP\n\t\t3. Get a Website IP\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	if chose=="1":
		print(yellow+"\n\n")
		ipt()

	elif chose=="2":
		
		ip=input(rosy+"Enter Target IP: ")
		print(yellow+"\n\n")
		ipt(ip)

	elif chose=="3":
		os.system('clear')
		wb=input(rosy+"\nEnter Target Website: "+red)
		ip=socket.gethostbyname(wb)
		print(yellow+"\nYour Website IP is: "+ip)
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	elif chose=="00":
		break
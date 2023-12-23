# Coded by Cracker
# CRACKER911181
 


import os,time
try:
	import youtube_dl
except ModuleNotFoundError:
	os.system("pip install youtube_dl")
from youtube_dl import *




def yt():
	
	link=str(input("\n Enter Video Link: "))
	px=str(input(pest+"\n\t1.Download 360p\n\t2.Download 720p\n\t3.Download 1080p\n\t4.Download mp3\n\n Enter pixel: "))
	
	if px=="1":
		pixel="18"
		options={"format":""+pixel+""}
		
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)
	
	elif px=="2":
		pixel="22"
		options={"format":""+pixel+""}
#		link=str(input("\n Enter Video Link: "))
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)
	
	elif px=="3":
		pixel="137"
		options={"format":""+pixel+""}
#		link=str(input("\n Enter Url: "))
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)
	
	elif px=="4":
		pixel="140"
		options={"format":""+pixel+""}
#		link=str(input("\n Enter Url: "))
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)


#18 mp4 - 360p
#22 mp4 - 720p
#137 mp4 - 1080p without sound
#140 mp3 -audio only


def fb():
	
	try:
		link=str(input(rosy+"\n Enter Video Link: "))
		print(blue+"\n[+]Downloading Start")
		
		YoutubeDL().download([link])
		print(green+"\n\n     Download Done")
	except youtube_dl.utils.DownloadError:
		print(red+"\n⚠️This Video Maybe Private. This Tool can't Download Private Video⚠️   ")
		time.sleep(3.8)

#Text colour
#created By Cracker911181
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
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Downloader [★] \n"""+green+""" ========================================================="""+colouroff)
############################
	
	choose=str(input(pest+"\n\t\t1. YouTube Video Downloader\n\t\t2. Facebook Video Downloader\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if choose=="1":
		yt()
	elif choose=="2":
		fb()
	elif choose=="00":
		break
	
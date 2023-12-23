#Developed by Cracker911181
# Cracker911181




import os



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest




#os.system("pkg install p7zip")

def unzip():
	os.system("clear")
	zipfile = str(input(rosy+"\n\nEnter Your ZIP File Path with File name: ")).rstrip()
	
	try:
		open(zipfile,"rb").read()
		wantpwdown = str(input(rosy+"You Want To Use Your Wordlist (y/n): ")).rstrip()
		
		if ("Y" in wantpwdown) or "y" in wantpwdown:
			while True:
				pwdlistinp = str(input(rosy+"\nEnter Your Passwordlist Location with Filename: ")).rstrip()
				
				try:
					open(pwdlistinp,"r").read()
					break
				except FileNotFoundError:
					print(red+"\n\tYou entered a invalid file path!!")
			
			allpwd = "\n"+(open(pwdlistinp,"r").read())
		else:
			allpwd = "\n"+(open("/data/data/com.termux/files/home/Cracker-Tool/.test/pwdlist.txt","r").read())
			
	
		for pwd in allpwd.split("\n"):
			os.system("7z x "+zipfile+" -p"+str(pwd)+" -Y >pwdtest.txt")
		
			if "Everything is Ok" in (open("pwdtest.txt","r").read()):
				print(green+"\n\n\n\tYour Password is: "+yellow+str(pwd))
				os.system("rm -rf pwdtest.txt")
				input(blue+"\n\n       Press Enter To Back Previous Menu ")
				break
	
	except FileNotFoundError:
		print(red+"\n\n\tYou entered a invalid file path!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")




#unzip()


while True:
        

        os.system('clear')
        print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t        """+blue+"""[★] Zip File Cracker [★] \n"""+green+""" ========================================================="""+colouroff)
        chose=str(input(pest+"\n\t\t1. Crack Zip Password"+red+"\n\t\t00. Back To Home\n\n"+rosy+"Enter Your Option: "))
        
        if chose=="1":
        	try:
        		os.system("clear")
        		unzip()
        	except:
        		print(red+"\n\n\t\tSomething Went Wrong!!")
        		input(blue+"\n\n       Press Enter To Back Previous Menu ")
        
        elif chose == "00":
        	break
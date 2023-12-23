# Coded by Cracker
# CRACKER911181



import os,sys,time


version=open("/data/data/com.termux/files/home/Cracker-Tool/.test/version.txt","r").read()

#version="5.0"

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



exec((open("/data/data/com.termux/files/home/Cracker-Tool/cntrl.py","r")).read())

os.system("mv /data/data/com.termux/files/home/Cracker-Tool/.test/cracker /data/data/com.termux/files/usr/bin")

os.system("chmod +x /data/data/com.termux/files/usr/bin/cracker")


os.system("clear")

print(blue1+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue1+"""| |   | "__/ _` |/ __| |/ / _ \ "__|____| |/ _ \ / _ \| |
 """+pest1+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green1+"""             Crack Your World, If You Can\n\n\t\t      """+yellow1+"""Version:"""+red+version+""""""+colouroff)

print(blue1+"\n ==========================================================")

print(rosy1+f"\n                                       ||         ||\n  # Cracker-Tool Set Successfully      ||   "+green1+version+rosy1+"   ||\n  # Type: '"+colouroff+rosy+"cracker"+rosy1+"' For Run This Tool  ||"+red+" cracker "+rosy1+"||\n  # command:  "+colouroff+rosy+"cracker"+rosy1+"                  ||  "+red+"911181"+colouroff+rosy1+" ||\n                                       ||         ||\n"+colouroff)


print(blue+" ==========================================================")

sys.exit()
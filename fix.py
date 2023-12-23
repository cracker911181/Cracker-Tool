# Coded by Cracker
# CRACKER911181
 


import requests,sys,os
from threading import Thread as pool





#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest


link=str(input(pest+"\n\nEnter Target URL: "))

#### checking vulnarbility######
try:
	resp=requests.get(link+"'",headers={"User-Agent": "XY"}).text
	if "Unknown"  in resp or "Undefined" in resp or "error" in resp or "Error" in resp:
		print(green+"\n             ✅Your Link is Vulnarable✅   "+yellow)
		link_opn=open(".link.txt","w")
		link_opn.write(link)
		link_opn.close()
		pass
	
	else:
		sys.exit()

except requests.exceptions.ConnectionError:
	print(red+"\n            ❌Link is Not Vulnarable❌   ")
	sys.exit()
except requests.exceptions.MissingSchema:
	print(red+"\n             ⚠️Link Not Valid⚠️    ")
	sys.exit()

#############################

print(blue+"\n\n[+]Fixing URL Error\n"+yellow)

#############################

def fix0():
	opn=open(".symbol.txt","r")
	red=opn.read()
	sp=red.split("\n")
	
	
	
	for split in sp:
		fix_url=str(link+split)
		fix_resp=requests.get(fix_url,headers={"User-Agent": "XY"}).text
		
		if "Unknown"  in fix_resp or "Undefined" in fix_resp or "error" in fix_resp or "Error" in fix_resp:
			pass
		else:
			print(fix_url)
			symbol_opn=open(".smbl.txt","w")
			symbol_opn.write(split)
			symbol_opn.close()
			
			fix_opn=open(".fixlink.txt","w")
			fix_opn.write(fix_url)
			fix_opn.close()
			sys.exit()

##############################



t0=pool(target=fix0)

t0.start()

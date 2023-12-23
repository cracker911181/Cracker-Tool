
# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD

import os,time,sys

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



def dot(user):
	lnusr=len(user)
	
	dot=open("/data/data/com.termux/files/home/Cracker-Tool/.test/dlist.txt","r").read()
	spdot=dot.split("\n")
	x=1
	
	for new in spdot:
		for next in range(lnusr):
			main1=((user[:x])+"."+(user[x:]))
		
			per=str(main1+new)
			print(per)
		
			if x==lnusr-1:
				x=1
			else:
				x=x+1

def main1():
	us=str(input(rosy+"Enter Your Gmail: "))
	user=us.split("@")
	print(yellow+"\n\n\t\tYour Genarated Gmail List\n\n"+pest)
	time.sleep(1)
	dot(user[0])

def main():
	main1()
	input(blue+"\n\n        Press Enter To Back Previous Menu ")

while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t        """+blue+"""[★] GMAIL Genarator [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Gmail Genarate(Dot & Plus Trick)\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	if chose=="1":
		os.system("clear")
		main()
		
	elif chose=="00":
		break
=======
import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cwoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCgpkZWYgZG90KHVzZXIpOgoJbG51c3I9bGVuKHVzZXIpCgkKCWRvdD1vcGVuKCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9DcmFja2VyLVRvb2wvLnRlc3QvZGxpc3QudHh0IiwiciIpLnJlYWQoKQoJc3Bkb3Q9ZG90LnNwbGl0KCJcbiIpCgl4PTEKCQoJZm9yIG5ldyBpbiB'
love = 'mpTEiqQbXPDyzo3VtozI4qPOcovOlLJ5aMFufoaImpvx6PtxWPJ1unJ4kCFtbqKAypyf6rS0cXlVhVvfbqKAypyg4By0cXDbWPDbWPDyjMKV9p3ElXT1unJ4kX25yqlxXPDxWpUWcoaDbpTIlXDbWPDbWPDycMvO4CG1foaImpv0kBtbWPDxWrQ0kPtxWPJIfp2H6PtxWPDy4CKteZDbXMTIzVT1unJ4kXPx6Pty1pm1mqUVbnJ5jqKDbpz9mrFfvEJ50MKVtJJ91pvOUoJScoQbtVvxcPty1p2IlCKImYaAjoTy0XPWNVvxXPKOlnJ50XUyyoTkiqlfvKT5poyk0KUEMo3IlVRqyozSlLKEyMPOUoJScoPOZnKA0KT5povVepTImqPxXPKEcoJHhp2kyMKNbZFxXPJEiqPu1p2IlJmOqXDbXMTIzVT1unJ4bXGbXPJ1unJ4kXPxXPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqz'
god = 'lvdXMgTWVudSAiKQoKd2hpbGUgVHJ1ZToKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQoYmx1ZStmIiIiCiAgIF9fX18gICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgXwogIC8gX19ffF8gX18gX18gXyAgX19ffCB8IF9fX19fIF8gX18gICB8XyAgIF98X18gICBfX18gfCB8CiAiIiIrYmx1ZSsiIiJ8IHwgICB8ICdfXy8gX2AgfC8gX198IHwvIC8gXyBcICdfX3xfX19ffCB8LyBfIFwgLyBfIFx8IHwKICIiIitwZXN0KyIiInwgfF9fX3wgfCB8IChffCB8IChfX3wgICA8ICBfXy8gfCB8X19fX198IHwgKF8pIHwgKF8pIHwgfAogIFxfX19ffF98ICBcX18sX3xcX19ffF98XF9cX19ffF98ICAgICAgIHxffFxfX18vIFxfX18vfF98XG5cbiAiIiIrZ3JlZW4rI'
destiny = 'vVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRqADHyZVRqyozSlLKEipvOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXPDbXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoyk0KUDkYvOUoJScoPOUMJ5upzS0MFuRo3DtWvODoUImVSElnJAeXIkhKUEpqPVepzIxXlVjZP4tDzSwnlOHolOVo21yVvglo3A5XlWpoykhEJ50MKVtJJ91pvOCpUEco246VPVcXDbWPtycMvOwnT9mMG09VwRvBtbWPJ9mYaA5p3EyoFtvL2kyLKVvXDbWPJ1unJ4bXDbWPDbWMJkcMvOwnT9mMG09VwNjVwbXPDyvpzIunj=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969


# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD
import pyshorteners as sh
import time,os,sys


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



def shorter():
	link=str(input(rosy+"\n\nEnter Your Link: "))
	
	s=sh.Shortener()
	real=str(s.tinyurl.short(link))
	print(yellow+"\nYour Shorten Link: "+real)
	input(blue+"\n\n      Press Enter To Back Previous Menu ")

def short():
	try:
		shorter()
	
	
	except:
		print(red+"\n\n\tSomething went wrong")
		time.sleep(5)
		


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] URL Shortner [★] \n"""+green+""" ========================================================="""+colouroff)
	
	
	chose=str(input(pest+"\n\n\t\t1. URL Shortner\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	
	if chose=="1":
		short()
	elif chose=="00":
		break
=======
import base64, codecs
magic = 'aW1wb3J0IHB5c2hvcnRlbmVycyBhcyBzaAppbXBvcnQgdGltZSxvcyxzeXMKCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKCmRlZiBzaG9ydGVyKCk6CglsaW5rPXN0cihpbnB1dChyb3N5KyJcblxuRW50ZXIgWW91ciBMaW5rOiAiKSkKCQoJcz1zaC5T'
love = 'nT9lqTIhMKVbXDbWpzIuoQ1mqUVbpl50nJ55qKWfYaAbo3W0XTkcozfcXDbWpUWcoaDbrJIfoT93XlWpoyyiqKVtH2uipaEyovOZnJ5eBvNvX3WyLJjcPtycoaO1qPuvoUIyXlWpoykhVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtcxMJLtp2uipaDbXGbXPKElrGbXPDymnT9lqTIlXPxXPDbWPtyyrTAypUD6PtxWpUWcoaDbpzIxXlWpoykhKUEGo21yqTucozptq2IhqPO3pz9hMlVcPtxWqTygMF5moTIypPt1XDbWPDbXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bW2AfMJSlWlxXPKOlnJ50XTWfqJHeMvVvVtbtVPOsK19sVPNtVPNtVPNtVPNtVPNtVS8t'
god = 'ICAgICAgICAgICAgICAgX19fX18gICAgICAgICAgIF8KICAvIF9fX3xfIF9fIF9fIF8gIF9fX3wgfCBfX19fXyBfIF9fICAgfF8gICBffF9fICAgX19fIHwgfAogIiIiK2JsdWUrIiIifCB8ICAgfCAnX18vIF9gIHwvIF9ffCB8LyAvIF8gXCAnX198X19fX3wgfC8gXyBcIC8gXyBcfCB8CiAiIiIrcGVzdCsiIiJ8IHxfX198IHwgfCAoX3wgfCAoX198ICAgPCAgX18vIHwgfF9fX19ffCB8IChfKSB8IChfKSB8IHwKICBcX19fX3xffCAgXF9fLF98XF9fX3xffFxfXF9fX3xffCAgICAgICB8X3xcX19fLyBcX19fL3xffFxuXG4gIiIiK2dyZWVuKyIiIiAgICAgICAgICAgICBDcmFjayBZ'
destiny = 'o3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0VPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tIIWZVSAbo3W0ozIlVSivzVIqVSkhVvVvX2qlMJIhXlVvVvN9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0vVvVeL29fo3Ilo2MzXDbWPtxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqQRhVSIFGPOGnT9lqT5ypykhKUEpqPVepzIxXlVjZP5PLJAeVSEiVRuioJIpoykhVvglo3A5XlWSoaEypvOMo3IlVR9jqTyiowbtVvxcPtxXPDbWnJLtL2uip2H9CFVkVwbXPDymnT9lqPtcPtyyoTyzVTAbo3AyCG0vZQNvBtbWPJWlMJSe'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

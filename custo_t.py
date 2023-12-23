# Coded by Cracker 
# CRACKER911181
 

<<<<<<< HEAD

import os,time,sys
colouroff="\x1b[00m"
red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Termux Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Set Termux Banner\n\t\t2.Change Background Color\n\t\t3.Change Font"+red+"\n\t\t00.Back To HOME\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		
		oo=open('banr_t.py',"r").read()
		os.system("clear")
		exec(oo)
		
	elif chose=="2":
		oo=open("colr_t.py","r").read()
		os.system("clear")
		exec(oo)
	
	elif chose=="3":
		oo=open("fnt_t.py","r").read()
		os.system("clear")
		exec(oo)
		
	elif chose=="00":
		break
=======
import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cwpjb2xvdXJvZmY9Ilx4MWJbMDBtIgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCgp3aGlsZSBUcnVlOgoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludChibHVlK2YiIiIKICAgX19fXyAgICAgICAgICAgICAgICBfICAgICAgICAgICAgICAgIF9fX19fICAgICAgICAgICBfCiAgLyBfX198XyBfXyB'
love = 'sKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyXlVvVajtsPNtVUjtW19sYlOsLPO8YlOsK3jtsP8tYlOsVSjtW19ssS9sK198VUjiVS8tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVPNtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ'
god = '91IENhblxuXG5cdCAgICAgICAgICIiIitibHVlKyIiIlvimIVdIFRlcm11eCBUb29sIFvimIVdIFxuIiIiK2dyZWVuKyIiIiA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iIiIrY29sb3Vyb2ZmKQoJCgljaG9zZT1zdHIoaW5wdXQocGVzdCsiXG5cblx0XHQxLlNldCBUZXJtdXggQmFubmVyXG5cdFx0Mi5DaGFuZ2UgQmFja2dyb3VuZCBDb2xvclxuXHRcdDMuQ2hhbmdlIEZvbnQiK3JlZCsiXG5cdFx0MDAuQmFjayBUbyBIT01FXG5cbiIrcm9zeSsiRW50ZXIgWW91ciBPc'
destiny = 'UEco246VPVcXDbWPtycMvOwnT9mMG09VwRvBtbWPDbWPJ9iCJ9jMJ4bW2WuoaWsqP5jrFpfVaVvXF5lMJSxXPxXPDyipl5mrKA0MJ0bVzAfMJSlVvxXPDyyrTIwXT9iXDbWPDbWMJkcMvOwnT9mMG09VwVvBtbWPJ9iCJ9jMJ4bVzAioUWsqP5jrFVfVaVvXF5lMJSxXPxXPDyipl5mrKA0MJ0bVzAfMJSlVvxXPDyyrTIwXT9iXDbWPtyyoTyzVTAbo3AyCG0vZlV6PtxWo289o3OyovtvMz50K3DhpUxvYPWlVvxhpzIuMPtcPtxWo3Zhp3ymqTIgXPWwoTIupvVcPtxWMKuyLluiolxXPDxXPJIfnJLtL2uip2H9CFVjZPV6PtxWLaWyLJf='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

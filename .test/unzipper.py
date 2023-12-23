#Developed by Cracker911181
# Cracker911181




<<<<<<< HEAD
import os



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest




#os.system("pkg install p7zip")

def unzip():
	os.system("clear")
	zipfile = str(input(rosy+"\n\nEnter Your ZIP File Path with File name: ")).rstrip()
	
	try:
		open(zipfile,"rb").read()
		wantpwdown = str(input(rosy+"You Want To Use Your Wordlist (y/n): ")).rstrip()
		
		if ("Y" in wantpwdown) or "y" in wantpwdown:
			while True:
				pwdlistinp = str(input(rosy+"\nEnter Your Passwordlist Location with Filename: ")).rstrip()
				
				try:
					open(pwdlistinp,"r").read()
					break
				except FileNotFoundError:
					print(red+"\n\tYou entered a invalid file path!!")
			
			allpwd = "\n"+(open(pwdlistinp,"r").read())
		else:
			allpwd = "\n"+(open("/data/data/com.termux/files/home/Cracker-Tool/.test/pwdlist.txt","r").read())
			
	
		for pwd in allpwd.split("\n"):
			os.system("7z x "+zipfile+" -p"+str(pwd)+" -Y >pwdtest.txt")
		
			if "Everything is Ok" in (open("pwdtest.txt","r").read()):
				print(green+"\n\n\n\tYour Password is: "+yellow+str(pwd))
				os.system("rm -rf pwdtest.txt")
				input(blue+"\n\n       Press Enter To Back Previous Menu ")
				break
	
	except FileNotFoundError:
		print(red+"\n\n\tYou entered a invalid file path!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")




#unzip()


while True:
        

        os.system('clear')
        print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t        """+blue+"""[★] Zip File Cracker [★] \n"""+green+""" ========================================================="""+colouroff)
        chose=str(input(pest+"\n\t\t1. Crack Zip Password"+red+"\n\t\t00. Back To Home\n\n"+rosy+"Enter Your Option: "))
        
        if chose=="1":
        	try:
        		os.system("clear")
        		unzip()
        	except:
        		print(red+"\n\n\t\tSomething Went Wrong!!")
        		input(blue+"\n\n       Press Enter To Back Previous Menu ")
        
        elif chose == "00":
        	break
=======
import base64, codecs
magic = 'aW1wb3J0IG9zCgoKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCgoKCiNvcy5zeXN0ZW0oInBrZyBpbnN0YWxsIHA3emlwIikKCmRlZiB1bnppcCgpOgoJb3Muc3lzdGVtKCJjbGVhciIpCgl6aXBmaWxlID0gc3RyKGlucHV0KHJvc3krIlxuXG5FbnRlciBZb3VyIFpJUCBGaWxlIFBhdGggd2l0aCBGaWxlIG5hbWU6ICIpKS5yc3RyaXAoKQoJCgl0cnk6CgkJb3Blbih6aXBmaWxlLCJyYiIpLnJlYWQoKQoJCXdhbnRwd2Rvd24gPSBzdHIoaW5wdXQocm9zeSsiWW91IFdhbnQgVG8gVXNlIFlvdXIgV29yZGxpc3QgKHkvbik6ICIpKS5yc3RyaXAoKQoJCQoJCWlmICgiWSIgaW4gd2FudHB3ZG93bikgb3IgInkiIGluIHdhbnRwd2Rvd246CgkJCXdoaWxlIFRydWU6CgkJCQlwd2RsaXN0aW5wID0gc3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBQYXNzd29yZGxp'
love = 'p3DtGT9wLKEco24tq2y0nPOTnJkyozSgMGbtVvxcYaWmqUWcpPtcPtxWPDxXPDxWPKElrGbXPDxWPDyipTIhXUO3MTkcp3EcoaNfVaVvXF5lMJSxXPxXPDxWPDyvpzIunjbWPDxWMKuwMKO0VRMcoTIBo3ETo3IhMRIlpz9lBtbWPDxWPKOlnJ50XUWyMPfvKT5pqSyiqFOyoaEypzIxVTRtnJ52LJkcMPOznJkyVUOuqTtuVFVcPtxWPDbWPDyuoTkjq2DtCFNvKT4vXluipTIhXUO3MTkcp3EcoaNfVaVvXF5lMJSxXPxcPtxWMJkmMGbXPDxWLJkfpUqxVQ0tVykhVvfbo3OyovtvY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY2uioJHiD3WuL2gypv1Ho29fYl50MKA0Y3O3MTkcp3DhqUu0VvjvpvVcYaWyLJDbXFxXPDxWPtxXPDyzo3VtpUqxVTyhVTSfoUO3MP5mpTkcqPtvKT4vXGbXPDxWo3Zhp3ymqTIgXPV3rvO4VPVerzyjMzyfMFfvVP1jVvgmqUVbpUqxXFfvVP1MVQ5jq2E0MKA0YaE4qPVcPtxWPtxWPJyzVPWSqzIlrKEbnJ5aVTymVR9eVvOcovNbo3OyovtvpUqxqTImqP50rUDvYPWlVvxhpzIuMPtcXGbXPDxWPKOlnJ50XTqlMJIhXlWpoykhKT5pqSyiqKVtHTSmp3qipzDtnKZ6VPVerJIfoT93X3A0pvujq2DcXDbWPDxWo3Zhp3ymqTIgXPWloFNgpzLtpUqxqTImqP50rUDvXDbWPDxW'
god = 'aW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCQkJCWJyZWFrCgkKCWV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjoKCQlwcmludChyZWQrIlxuXG5cdFlvdSBlbnRlcmVkIGEgaW52YWxpZCBmaWxlIHBhdGghISIpCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCgoKCiN1bnppcCgpCgoKd2hpbGUgVHJ1ZToKICAgICAgICAKCiAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICAgICAgcHJpbnQoYmx1ZStmIiIiCiAgIF9fX18gICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgXwogIC8gX19ffF8gX18gX18gXyAgX19ffCB8IF9fX19fIF8gX18gICB8XyAgIF98X18gICBfX18gfCB8CiAiIiIrYmx1ZSsiIiJ8IHwgICB8ICdfXy8gX2AgfC8gX198IHwvIC8gXyBcICdfX3xfX19ffCB8LyBfIFwgLyBfIFx8IHwKICIiIitwZXN0KyIiInwgfF9fX3wgfCB8IChffCB8IChfX3wgICA8ICBfXy8gfCB8X19fX198IHwgKF8pIHwgKF8pIHwgfAogIFxfX19ffF98ICBcX18sX3xcX19ffF98XF9cX19ffF98ICAgICAgIHxffFxfX18vIFxf'
destiny = 'K18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVSccpPOTnJkyVRAlLJAeMKVtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPvNtVPNtVPNtL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKUEpqQRhVRAlLJAeVSccpPODLKAmq29lMPVepzIxXlWpoyk0KUDjZP4tDzSwnlOHolOVo21yKT5povVepz9mrFfvEJ50MKVtJJ91pvOCpUEco246VPVcXDbtVPNtVPNtVNbtVPNtVPNtVTyzVTAbo3AyCG0vZFV6PvNtVPNtVPNtPKElrGbXVPNtVPNtVPNWPJ9mYaA5p3EyoFtvL2kyLKVvXDbtVPNtVPNtVNxWqJ56nKNbXDbtVPNtVPNtVNyyrTAypUD6PvNtVPNtVPNtPDyjpzyhqPulMJDeVykhKT5pqSk0H29gMKEbnJ5aVSqyoaDtI3WiozpuVFVcPvNtVPNtVPNtPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbtVPNtVPNtVNbtVPNtVPNtVTIfnJLtL2uip2HtCG0tVwNjVwbXVPNtVPNtVPNWLaWyLJf='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

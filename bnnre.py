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


def make():
	print(blue+"\n\tThis Tool Needed Storage Permission")
	os.system('termux-setup-storage')
	print(pest+"\n\t\tDONE")
	print(pest+"\n\tBanner Setup On Termux")
	nm=str(input(rosy+"\nEnter Your Name: "))
	print(pest+"\n\tSet Your Password")
	pd=str(input(rosy+"\nEnter Your Password: "))
	pd1=str(input("Confirm Your Password: "))
	os.system("rm -rf /data/data/com.termux/files/usr/etc/motd")
	oo=open("/data/data/com.termux/files/usr/etc/bnnr.py","w")
	if pd==pd1:
		print(green+"")
		print()
		print(pest+"Banner Set & User Termux Is Now Password Protected")
		time.sleep(2)
		a="""
def ban():
	import os,time,sys
	red="\x1b[91m"
	green="\x1b[92m"
	rosy="\x1b[95m"
	pest="\x1b[96m" #pest

	pas='"""+pd+"""'

	while True:
		os.system('clear')
		print(green+"")
		os.system('figlet """+nm+"""')
		print(pest+'			developed by cracker911181')
		pwd=str(input(rosy+"Enter Your Password: "))
		if pas==pwd:
			print()
			print(green+"	Login Successfull")
			time.sleep(1.5)
			os.system('clear')
			print(green+"")
			os.system('figlet """+nm+"""')
			print(pest+'			developed by cracker911181')
			break 
			sys.exit()
		else:
			print()
			print()
			print(red+"	Password Not Match")
			time.sleep(1.5)
try:
	ban()
except:
	ban()"""


		oo.write(a)
		oo1=open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
		oo1.write("PS1='$ '\npython /data/data/com.termux/files/usr/etc/bnnr.py \ncd $HOME")
	else:
		print(red+"")
		print()
		print("	Password Not Match")
		time.sleep(3)

while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Termux Banner [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Set Termux Banner"+red+"\n\t\t00.Back To HOME\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		try:
			make()
		except:
			make()
	
	elif chose=="00":
		break
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUsc3lzCmNvbG91cm9mZj0iXHgxYlswMG0iCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCmRlZiBtYWtlKCk6CglwcmludChibHVlKyJcblx0VGhpcyBUb29sIE5lZWRlZCBTdG9yYWdlIFBlcm1pc3Npb24iKQoJb3Muc3lzdGVtKCd0ZXJtdXgtc2V0dXAtc3RvcmFnZScpCglwcmludChwZXN0KyJcblx0XHRET05FIikKCXByaW50KHBlc3QrIlxuXHRCYW5uZXIgU2V0dXAgT24gVGVybXV4IikKCW5tPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgTmFtZTogIikpCglwcmludChwZXN0KyJcblx0U2V0IFlvdXIgUGFzc3dvcmQiKQoJcGQ9c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBQYXNzd29yZDogIikpCglwZDE9c3RyKGlucHV0KCJDb25maXJtIFlvdXIgUGFzc3dvcmQ6ICIpKQoJb3Muc3lzdGVtKCJybSAtcmYgL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9ldGMvbW90ZCIpCglvbz1vcGVuKCIvZGF0YS9kYXRhL2NvbS50ZXJ'
love = 'gqKtiMzyfMKZiqKAlY2I0Ll9voz5lYaO5VvjvqlVcPtycMvOjMQ09pTDkBtbWPKOlnJ50XTqlMJIhXlVvXDbWPKOlnJ50XPxXPDyjpzyhqPujMKA0XlWPLJ5hMKVtH2I0VPLtIKAypvOHMKWgqKttFKZtGz93VSOup3A3o3WxVSOlo3EyL3EyMPVcPtxWqTygMF5moTIypPtlXDbWPJR9VvVvPzEyMvOvLJ4bXGbXPJygpT9lqPOiplk0nJ1yYUA5pjbWpzIxCFWprQSvJmxkoFVXPJqlMJIhCFWprQSvJmxloFVXPKWip3x9Vyk4ZJWoBGIgVtbWpTImqQ0vKUtkLyf5Az0vVPAjMKA0PtbWpTSmCFpvVvVepTDeVvVvWjbXPKqbnJkyVSElqJH6PtxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWpUWcoaDbM3WyMJ4eVvVcPtxWo3Zhp3ymqTIgXPqznJqfMKDtVvVvX25gXlVvVvpcPtxWpUWcoaDbpTImqPfaPDxWMTI2MJkipTIxVTW5VTAlLJAeMKV5ZGRkBQRaXDbWPKO3MQ1mqUVbnJ5jqKDbpz9mrFfvEJ50MKVtJJ91pvODLKAmq29lMQbtVvxcPtxWnJLtpTSmCG1jq2D6PtxWPKOlnJ50XPxXPDxWpUWcoaDbM3WyMJ4eVtyZo2qcovOGqJAwMKAmMaIfoPVcPtxWPKEcoJHhp2kyMKNbZF41XDbWPDyipl5mrKA0MJ0bW2AfMJSlWlxXPDxWpUWcoaDbM3WyMJ4eVvVcPtxWPJ9mYaA5p3EyoFtaMzyaoT'
god = 'V0ICIiIitubSsiIiInKQoJCQlwcmludChwZXN0KycJCQlkZXZlbG9wZWQgYnkgY3JhY2tlcjkxMTE4MScpCgkJCWJyZWFrIAoJCQlzeXMuZXhpdCgpCgkJZWxzZToKCQkJcHJpbnQoKQoJCQlwcmludCgpCgkJCXByaW50KHJlZCsiCVBhc3N3b3JkIE5vdCBNYXRjaCIpCgkJCXRpbWUuc2xlZXAoMS41KQp0cnk6CgliYW4oKQpleGNlcHQ6CgliYW4oKSIiIgoKCgkJb28ud3JpdGUoYSkKCQlvbzE9b3BlbigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9ldGMvYmFzaC5iYXNocmMiLCJ3IikKCQlvbzEud3JpdGUoIlBTMT0nJCAnXG5weXRob24gL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9ldGMvYm5uci5weSBcbmNkICRIT01FIikKCWVsc2U6CgkJcHJpbnQocmVkKyIiKQoJCXByaW50KCkKCQlwcmludCgiCVBhc3N3b3JkIE5vdCBNYXRjaCIpCgkJdGltZS5zbGVlcCgzKQoKd2hpbGUgVHJ1ZToKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQoYmx1ZStmIiIiCiAgIF9fX18gICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgXwogIC8gX19ffF8gX18gX18gXyAgX19ffCB8IF9fX19fIF8gX18gICB8XyAgIF98X18gI'
destiny = 'POsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNvVvVeLzk1MFfvVvWo4cvSKFOHMKWgqKttDzShozIlVSivzVIqVSkhVvVvX2qlMJIhXlVvVvN9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0vVvVeL29fo3Ilo2MzXDbWPtywnT9mMG1mqUVbnJ5jqKDbpTImqPfvKT5poyk0KUDkYyAyqPOHMKWgqKttDzShozIlVvglMJDeVykhKUEpqQNjYxWuL2ftIT8tFR9AEIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWnJLtL2uip2H9CFVkVwbXPDy0pax6PtxWPJ1un2HbXDbWPJI4L2IjqQbXPDxWoJSeMFtcPtxXPJIfnJLtL2uip2H9CFVjZPV6PtxWLaWyLJf='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

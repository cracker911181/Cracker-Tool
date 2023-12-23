# Coded by Cracker 
# CRACKER911181 

# last

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
	from cracker_say import bennar
	red="\x1b[91m"
	green="\x1b[92m"
	rosy="\x1b[95m"
	pest="\x1b[96m" #pest

	pas='"""+pd+"""'

	while True:
		os.system('clear')
		print(green+"")
		
		colouroff="\x1b[00m" 
		red1="\x1b[41m" #red1

		os.system("python /data/data/com.termux/files/usr/etc/andro.py")
		
		print()
		
		print()
		pwd=str(input(rosy+"Enter Your Password: "))
		if pas==pwd:
			print()
			print(green+"	Login Successfull")
			time.sleep(1.2)
			os.system('clear')
			print(colouroff+"")
			bennar('"""+nm+"""')
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
		os.system("mv andro.py /data/data/com.termux/files/usr/etc")
	else:
		print(red+"")
		print()
		print("	Password Not Match")
		time.sleep(3)
	

try:
	make()
except:
	make()
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUsc3lzCmNvbG91cm9mZj0iXHgxYlswMG0iCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCmRlZiBtYWtlKCk6CglwcmludChibHVlKyJcblx0VGhpcyBUb29sIE5lZWRlZCBTdG9yYWdlIFBlcm1pc3Npb24iKQoJb3Muc3lzdGVtKCd0ZXJtdXgtc2V0dXAtc3RvcmFnZScpCglwcmludChwZXN0KyJcblx0XHRET05FIikKCXByaW50KHBlc3QrIlxuXHRCYW5uZXIgU2V0dXAgT24gVGVybXV4IikKCW5tPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgTmFtZTogIikpCglwcmludChwZXN0KyJcblx0U2V0IFlvdXIgUGFzc3dvcmQiKQoJcGQ9c3RyKGlucHV0KHJvc3krIlxuRW5'
love = '0MKVtJJ91pvODLKAmq29lMQbtVvxcPtyjMQR9p3ElXTyhpUI0XPWQo25znKWgVSyiqKVtHTSmp3qipzD6VPVcXDbWo3Zhp3ymqTIgXPWloFNgpzLtY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY3Impv9yqTZioJ90MPVcPtyiom1ipTIhXPViMTS0LF9xLKEuY2AioF50MKWgqKtiMzyfMKZiqKAlY2I0Ll9voz5lYaO5VvjvqlVcPtycMvOjMQ09pTDkBtbWPKOlnJ50XTqlMJIhXlVvXDbWPKOlnJ50XPxXPDyjpzyhqPujMKA0XlWPLJ5hMKVtH2I0VPLtIKAypvOHMKWgqKttFKZtGz93VSOup3A3o3WxVSOlo3EyL3EyMPVcPtxWqTygMF5moTIypPtlXDbWPJR9VvVvPzEyMvOvLJ4bXGbXPJygpT9lqPOiplk0nJ1yYUA5pjbWMaWioFOwpzSwn2IlK3AurFOcoKOipaDtLzIhozSlPtylMJD9Vyk4ZJWoBGSgVtbWM3WyMJ49Vyk4ZJWoBGWgVtbWpz9mrG0vKUtkLyf5AJ0vPtyjMKA0CFWprQSvJmx2oFVtV3'
god = 'Blc3QKCglwYXM9JyIiIitwZCsiIiInCgoJd2hpbGUgVHJ1ZToKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChncmVlbisiIikKCQkKCQljb2xvdXJvZmY9Ilx4MWJbMDBtIiAKCQlyZWQxPSJceDFiWzQxbSIgI3JlZDEKCgkJb3Muc3lzdGVtKCJweXRob24gL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9ldGMvYW5kcm8ucHkiKQoJCQoJCXByaW50KCkKCQkKCQlwcmludCgpCgkJcHdkPXN0cihpbnB1dChyb3N5KyJFbnRlciBZb3VyIFBhc3N3b3JkOiAiKSkKCQlpZiBwYXM9PXB3ZDoKCQkJcHJpbnQoKQoJCQlwcmludChncmVlbisiCUxvZ2luIFN1Y2Nlc3NmdWxsIikKCQkJdGltZS5zbGVlcCgxLjIpCgkJCW9zLnN5c3RlbSgnY2xlYXInKQoJCQlwcmludChjb2xvdXJvZmYrIiIpCgkJCWJlbm5hcignIiIiK25tKyIiIicpCgkJCWJyZWFrIAoJCQlzeXMuZXhpdCgpCgkJZWxzZToKC'
destiny = 'DxWpUWcoaDbXDbWPDyjpzyhqPtcPtxWPKOlnJ50XUWyMPfvPIOup3A3o3WxVR5iqPOALKEwnPVcPtxWPKEcoJHhp2kyMKNbZF41XDc0pax6PtyvLJ4bXDcyrTAypUD6PtyvLJ4bXFVvVtbXPtxWo28hq3WcqTHbLFxXPDyiomR9o3OyovtvY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY3Impv9yqTZiLzSmnP5vLKAbpzZvYPW3VvxXPDyiomRhq3WcqTHbVyOGZG0aWPNaKT5jrKEbo24tY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY3Impv9yqTZiLz5hpv5jrFOpozAxVPEVG01SVvxXPDyipl5mrKA0MJ0bVz12VTShMUWiYaO5VP9xLKEuY2EuqTRiL29gYaEypz11rP9znJkypl91p3ViMKEwVvxXPJIfp2H6PtxWpUWcoaDbpzIxXlVvXDbWPKOlnJ50XPxXPDyjpzyhqPtvPIOup3A3o3WxVR5iqPOALKEwnPVcPtxWqTygMF5moTIypPtmXDbWPtc0pax6PtygLJgyXPxXMKuwMKO0BtbWoJSeMFtcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

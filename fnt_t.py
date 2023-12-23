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

def color():
	
	print(pest+"""
	1.FiraCode
	2.Source-Code-Pro
	3.Go
	4.Fantasque
	5.Iosevka
	6.OpenDyslexic
	7.Hermit
	8.Inconsolata
	9.Monofur
	10.Meslo
	11.DejaVu
	12.Monoid
	13.Hack
	14.Roboto
	15.Ubuntu
	16.Courier-Prime
	17.LiberationMono
	18.Fira
	19.Anonymous-Pro
	20.GNU-FreeFont
       """+green+"""	21.Reset Fonts""")
	
	chose=str(input(rosy+"\n\nEnter Your Color: "))
	
	
	if chose=="21":
		os.system("rm -rf /data/data/com.termux/files/home/.termux/font.ttf")
			
	else:

		open("/data/data/com.termux/files/home/Cracker-Tool/.ctermux/font/"+chose+".ttf","r")
		os.system("cp /data/data/com.termux/files/home/Cracker-Tool/.ctermux/font/"+chose+".ttf /data/data/com.termux/files/home/.termux")
		os.system("mv /data/data/com.termux/files/home/.termux/"+chose+".ttf /data/data/com.termux/files/home/.termux/font.ttf")


while True:
	os.system("clear")
	try:
		color()
		print(yellow+"\n\n\t\tDone")
		time.sleep(5)
		break
	except FileNotFoundError:
		
		print(red+"\n\n\tInvalid Color Number")
		time.sleep(2)
		
		pass
	except PermissionError:
		pass
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUsc3lzCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgpkZWYgY29sb3IoKToKCQoJcHJpbnQocGVzdCsiIiIKCTEuRmlyYUNvZGUKCTIuU291cmNlLUNvZGUtUHJvCgkzLkdvCgk0LkZhbnRhc3F1ZQoJNS5Jb3NldmthCgk'
love = '2Yx9jMJ5RrKAfMKucLjbWAl5VMKWgnKDXPGthFJ5wo25mo2kuqTRXPGxhGJ9ho2M1ptbWZGNhGJImoT8XPGRkYxEynzSJqDbWZGVhGJ9ho2yxPtxkZl5VLJAePtxkAP5Fo2WiqT8XPGR1YyIvqJ50qDbWZGLhD291pzyypv1DpzygMDbWZGphGTyvMKWuqTyiox1ioz8XPGR4YxMcpzRXPGR5YxSho255oJ91pl1Dpz8XPGVjYxqBIF1TpzIyEz9hqNbtVPNtVPNtVvVvX2qlMJIhXlVvVtxlZF5FMKAyqPOTo250plVvVvxXPDbWL2uip2H9p3ElXTyhpUI0XUWip3xeVykhKT5SoaEypvOMo3IlVRAioT9lBvNvXFxXPDbWPtycMvOwnT9mMG09VwVkVwbXPDyipl5mrKA0MJ0bVaWgVP'
god = '1yZiAvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS8udGVybXV4L2ZvbnQudHRmIikKCQkJCgllbHNlOgoKCQlvcGVuKCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9DcmFja2VyLVRvb2wvLmN0ZXJtdXgvZm9udC8iK2Nob3NlKyIudHRmIiwiciIpCgkJb3Muc3lzdGVtKCJjcCAvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9DcmFja2VyLVRvb2wvLmN0ZXJtdXgvZm9udC8iK2Nob3NlKyIudHRmIC9kYXRhL2RhdGEvY29tLnRlcm11eC9maWxlcy9ob21lLy50ZXJtdXgiKQoJCW9zLnN5c3RlbSgibXYgL2RhdGEvZGF0YS9jb20udGVyb'
destiny = 'KI4Y2McoTImY2uioJHiYaEypz11rP8vX2Abo3AyXlVhqUEzVP9xLKEuY2EuqTRiL29gYaEypz11rP9znJkypl9bo21yYl50MKWgqKtiMz9hqP50qTLvXDbXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bVzAfMJSlVvxXPKElrGbXPDywo2kipvtcPtxWpUWcoaDbrJIfoT93XlWpoykhKUEpqREiozHvXDbWPKEcoJHhp2kyMKNbAFxXPDyvpzIunjbWMKuwMKO0VRMcoTIBo3ETo3IhMRIlpz9lBtbWPDbWPKOlnJ50XUWyMPfvKT5poyk0FJ52LJkcMPOQo2kipvOBqJ1vMKVvXDbWPKEcoJHhp2kyMKNbZvxXPDxXPDyjLKAmPtyyrTAypUDtHTIloJymp2yioxIlpz9lBtbWPKOup3Z='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

#Developed By CRACKER911181
# Coded By Cracker911181

<<<<<<< HEAD
import os,time,random,requests

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

def ccGen():
	totaldigits=16
	
	inputcvc = int (input(rosy+"\n\nEnter Bin : "))
	totalcc = int (input(rosy+"Number of CC : "))
	lapart = str (inputcvc)
	if len(lapart)==0:
		count = 16
	count = len (str (inputcvc))
	totalbin =  int (count)
	genbin = totaldigits-totalbin
	firstnum =  "1"*genbin
	lastnum = "9"*genbin
	binf =  int (firstnum)
	binl = int (lastnum)
	b = 0
	print("\n\n")
	for i in range (totalcc):
		rancc=str(random.randint(binf,binl))
		cc=lapart+rancc
		ranmonth = str (random.randint (1,12))
		smon =str (ranmonth)
		if len(smon)==1:
			month = "0"+smon
			b = month
		else  :
			month =smon
			b = month
		ranyear = str (random.randint(2022,2025))
		cvc = str (random.randint(111,999))
		validcc=cc+"|"+month+"|"+ranyear+"|"+cvc
		
		print(yellow+"\t"+validcc)
		





def ccck():
	
	cc=str(input(rosy+"\n\nEnter a CC For Check: "))
	if int(cc[0])<4 or int(cc[0])>6:
		print(red+"\n\n\n\t\tYou Entered a Invalid CC!!")
	
	else:
	
		appi=requests.get("https://lookup.binlist.net/"+cc).json()
#	print(appi)
#	except json.decoder.JSONDecodeError:
		
		
	
		schema=str(appi["scheme"])
		type=str(appi["type"])
		try:
			brand=str(appi["brand"])
		except:
			brand="Unknown"
	
		cntry=(appi["country"])
		cname=str(cntry["name"])
		cemoji=str(cntry["emoji"])
		c_curncy=str(cntry["currency"])
		namric=str(cntry["numeric"])
		alpha2=str(cntry["alpha2"])
		clati=str(cntry["latitude"])
		clong=str(cntry["longitude"])
	
		try:
			bnk=(appi["bank"])
		
			try:
				bname=str(bnk["name"])
			except:
				bname="Unknown"
			
			try:
				burl=str(bnk["url"])
			except:
				burl="Unknown"
		
			try:
				bphn=str(bnk['phone'])
			except:
				bphn="Unknown"
		
			try:
				bcity=str(bnk['city'])
			except:
				bcity="Unknown"
			
		except:
			bname="Unknown"
			burl="Unknown"
			bphn="Unknown"
			bcity="Unknown"
		
		main=str(yellow+"\n\nCC → "+cc+" \n\n|\n| Scheme: "+schema+"\n| Type:   "+type+"\n| Brand:  "+brand+"\n|\n| Country |\n          | Name:      "+cname+"\n          | Emoji:     "+cemoji+"\n          | Currency:  "+c_curncy+"\n          | Numeric:   "+namric+"\n          | Alpha2:    "+alpha2+"\n          | Latitude:  "+clati+"\n          | Longitude: "+clong+"\n\n|\n| Bank |\n       | Name:  "+bname+"\n       | URL:   "+burl+"\n       | Phone: "+bphn+"\n       | City:  "+bcity)
		print(main)
		







while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Anon Share [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Check Cradit Card Number(CC)\n\t\t2.Genarate Random CC\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		os.system("clear")
		try:
			ccck()
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		except requests.exceptions.ConnectionError:
			print(red+"\n\n\t   Check Your Internet Connection!!")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
		except:
			print(red+"\n\n\t\tSomething Went Worng!!")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
			
	elif chose=="2":
		os.system("clear")
		try:
			ccGen()
		except:
			print(red+"\n\n\t\tSomething Went Worng!!")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
	elif chose=="00":
		break
	
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUscmFuZG9tLHJlcXVlc3RzCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgpkZWYgY2NHZW4oKToKCXRvdGFsZGlnaXRzPTE2CgkKCWlucHV0Y3ZjID0gaW50IChpbnB1dChyb3N5KyJcblxuRW50ZXIgQmluIDogIikpCgl0b3RhbGNjID0gaW50IChpbnB1dChyb3N5KyJOdW1iZXIgb2YgQ0MgOiAiKSkKCWxhcGFydCA9IHN0ciAoaW5wdXRjdmMpCglpZiBsZW4obGFwYXJ0KT09MDoKCQljb3VudCA9IDE2Cgljb3VudCA9IGxlbiAoc3RyIChpbnB1dGN2YykpCgl0b3RhbGJpbiA9ICBpbnQgKGNvdW50KQoJZ2VuYmluID0gdG90YWxkaWdpdHMtdG90YWxiaW4KCWZpcnN0bnVtID0gICIxIipnZW5iaW4KCWxhc3RudW0gPSAiOSIqZ2VuYmluCgliaW5mID0gIGludCAoZmlyc3RudW0pCgliaW5sID0gaW50IChsYXN0bnVtKQoJYiA9IDAKCXByaW50KCJcblxuIikKCWZvciBpIGluIHJhbmdlICh0b3RhbGNjKToKCQlyYW5jYz1zdHIocmFuZG9tLnJhbmRpbnQoYmluZixiaW5sKSkKCQljYz1sYXBhcnQrcmFuY2MKCQlyYW5tb250aCA9IHN0ciAocmFuZG9tLnJhbmRpbnQgKDEsMTIpKQoJCXNtb24gPXN0ciAocmFubW9udGgpCgkJaWYgbGVuKHNtb24pPT0xOgoJCQltb250aCA9ICIwIitzbW9uCgkJCWIgPSBtb250aAoJCWVsc2UgIDoKCQkJbW9udGggPXNtb24KCQkJYiA9IG1vbnRoCgkJcmFueWVhciA9IHN0ciAocmFuZG9tLnJhbmRpbnQoMjAyMiwyMDI1KSkKCQljdmMgPSBzdHIgKHJhbmRvbS5yYW5kaW50KDExMSw5OTkpKQoJCXZhbGlkY2M9Y2MrInwiK21vbnRoKyJ8IityYW55Z'
love = 'JSlXlW8VvgwqzZXPDxXPDyjpzyhqPu5MJkfo3peVyk0Vvg2LJkcMTAwXDbWPDbXPtbXPzEyMvOwL2AeXPx6PtxXPJAwCKA0pvucoaO1qPulo3A5XlWpoykhEJ50MKVtLFOQDlOTo3VtD2uyL2f6VPVcXDbWnJLtnJ50XTAwJmOqXGj0VT9lVTyhqPuwL1fjKFx+AwbXPDyjpzyhqPulMJDeVykhKT5poyk0KUEMo3HtEJ50MKWyMPOuVRyhqzSfnJDtD0ZuVFVcPtxXPJIfp2H6PtxXPDyupUOcCKWypKIyp3EmYzqyqPtvnUE0pUZ6Yl9fo29eqKNhLzyhoTymqP5hMKDiVvgwLlxhnaAiovtcPvZWpUWcoaDbLKOjnFxXVjyyrTAypUDtnaAiov5xMJAiMTIlYxcGG05RMJAiMTISpaWipwbXPDxXPDxXPDbWPKAwnTIgLG1mqUVbLKOjnIfvp2AbMJ1yVy0cPtxWqUyjMG1mqUVbLKOjnIfvqUyjMFWqXDbWPKElrGbXPDxWLaWuozD9p3ElXTSjpTyoVzWlLJ5xVy0cPtxWMKuwMKO0BtbWPDyvpzShMQ0vIJ5eoz93ovVXPDbWPJAhqUW5CFuupUOcJlWwo3IhqUW5Vy0cPtxWL25uoJH9p3ElXTAhqUW5JlWhLJ1yVy0cPtxWL2Igo2ccCKA0pvuwoaElrIfvMJ1inzxvKFxXPDywK2A1pz5wrG1mqUVbL250payoVzA1paWyozA5Vy0cPtxWozSgpzywCKA0pvuwoaElrIfvoaIgMKWcLlWqXDbWPJSfpTuuZw1mqUVbL250payoVzSfpTuuZvWqXDbWPJAfLKEcCKA0pvuwoaElrIfvoTS0nKE1MTHvKFxXPDywoT9hMm1mqUVbL250payoVzkiozqcqUIxMFWqXDbWPtxWqUW5BtbWPDyvozf9XTSjpTyoVzWuozfvKFxXPDxXPDxWqUW5BtbWPDxWLz5uoJH9p3ElXTWhn1fvozSgMFWqXDbWPDyyrTAypUD6PtxWPDyvozSgMG0vIJ5eoz93ovVXPDxWPtxWPKElrGbXPDxWPJW1pzj9p3ElXTWhn1fvqKWfVy0cPtxWPJI4L2IjqQbXPDxWPJW1pzj9VyIhn25iq24vPtxWPtxWPKElrGbXPDxWPJWjnT49p3ElXTWhn1fapTuiozHaKFxXPDxWMKuwMKO0BtbWPDxWLaObow0vIJ5eoz93ovVXPDxXPDxWqUW5BtbWPDxWLzAcqUx9p3ElXTWhn1faL2y0rFqqXDbWPDyyrTAypUD6Pt'
god = 'kJCQliY2l0eT0iVW5rbm93biIKCQkJCgkJZXhjZXB0OgoJCQlibmFtZT0iVW5rbm93biIKCQkJYnVybD0iVW5rbm93biIKCQkJYnBobj0iVW5rbm93biIKCQkJYmNpdHk9IlVua25vd24iCgkJCgkJbWFpbj1zdHIoeWVsbG93KyJcblxuQ0Mg4oaSICIrY2MrIiBcblxufFxufCBTY2hlbWU6ICIrc2NoZW1hKyJcbnwgVHlwZTogICAiK3R5cGUrIlxufCBCcmFuZDogICIrYnJhbmQrIlxufFxufCBDb3VudHJ5IHxcbiAgICAgICAgICB8IE5hbWU6ICAgICAgIitjbmFtZSsiXG4gICAgICAgICAgfCBFbW9qaTogICAgICIrY2Vtb2ppKyJcbiAgICAgICAgICB8IEN1cnJlbmN5OiAgIitjX2N1cm5jeSsiXG4gICAgICAgICAgfCBOdW1lcmljOiAgICIrbmFtcmljKyJcbiAgICAgICAgICB8IEFscGhhMjogICAgIithbHBoYTIrIlxuICAgICAgICAgIHwgTGF0aXR1ZGU6ICAiK2NsYXRpKyJcbiAgICAgICAgICB8IExvbmdpdHVkZTogIitjbG9uZysiXG5cbnxcbnwgQmFuayB8XG4gICAgICAgfCBOYW1lOiAgIitibmFtZSsiXG4gICAgICAgfCBVUkw6ICAgIitidXJsKyJcbiAgICAgICB8IFBob25lOiAiK2JwaG4rIlxuICAgICAgIHwgQ2l0eTogICIrYmNpdHkpCgkJcHJpbnQobWFpbikKCQkKCgoKCgoKCndoaWxlIFRydWU6Cglvcy5zeXN0ZW0oJ2NsZWFyJykKCXByaW50KGJsdWUrZiIiIgogICBfX19fICAgICAgICAgICAgICAgIF8gICAgICAgICAgICAgICAgX19fX18gICAgICAgICAgIF8KICAvIF9fX3xfIF9fIF9fIF8gIF9fX3wgfCBfX19fXyBfIF9fICAgfF8gICBffF9fICAgX19fIHwgfAogIiIiK2JsdWUrIiIifCB8ICAgfCAnX18vIF9gIHwvIF9ffCB8LyAvIF8gXCAnX198X19fX3wgfC8gXyBcIC8gXyBcfCB8CiAiIiIrcGVzdCsiIiJ8IHxfX198IHwgfCAoX3wgfCAoX198ICAgPCAgX18vIHwgfF9fX19ffCB8IChfKSB8IChfKSB8IHwKICBcX19fX3xffCAgXF9fLF98XF9fX3xffFxfXF9fX3xffCAgICAgICB8X3xcX19fLyB'
destiny = 'pK19sY3kssSkhKT4tVvVvX2qlMJIhXlVvVvNtVPNtVPNtVPNtVPOQpzSwnlOMo3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0VPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRSho24tH2uupzHtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqQRhD2uyL2ftD3WuMTy0VRAupzDtGaIgLzIlXRAQXIkhKUEpqQVhE2IhLKWuqTHtHzShMT9gVRAQKT5pqSk0VvglMJDeVwNjYxWuL2ftIT8tFT9gMIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWnJLtL2uip2H9CFVkVwbXPDyipl5mrKA0MJ0bVzAfMJSlVvxXPDy0pax6PtxWPJAwL2fbXDbWPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWPJI4L2IjqPOlMKS1MKA0pl5yrTAypUEco25mYxAioz5yL3Eco25SpaWipwbXPDxWpUWcoaDbpzIxXlWpoykhKUDtVPOQnTIwnlOMo3IlVRyhqTIlozI0VRAioz5yL3Eco24uVFVcPtxWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtxWPtxWMKuwMKO0BtbWPDyjpzyhqPulMJDeVykhKT5pqSk0H29gMKEbnJ5aVSqyoaDtI29lozpuVFVcPtxWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtxWPDbWMJkcMvOwnT9mMG09VwVvBtbWPJ9mYaA5p3EyoFtvL2kyLKVvXDbWPKElrGbXPDxWL2AUMJ4bXDbWPJI4L2IjqQbXPDxWpUWcoaDbpzIxXlWpoykhKUEpqSAioJI0nTyhMlOKMJ50VSqipz5aVFRvXDbWPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWPDbWMJkcMvOwnT9mMG09VwNjVwbXPDyvpzIunjbW'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

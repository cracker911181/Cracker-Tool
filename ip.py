<<<<<<< HEAD
import requests
import socket
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




def ipt(ipp=""):
	try:
		api=requests.get("http://ip-api.com/json/"+ipp).json()
	
		tip=str(api["query"])
		status=str(api["status"])
		cntry=str(api["country"])
		cntrycd=str(api["countryCode"])
		region=str(api["region"])
		regionnam=str(api["regionName"])
		city=str(api["city"])
		zip=str(api["zip"])
		lat=str(api["lat"])
		lon=str(api["lon"])
		timezone=str(api["timezone"])
		isp=str(api["isp"])
		org=str(api["org"])
		ass=str(api["as"])
		map=str("https://www.google.com/maps/place/"+str(lat)+"+"+str(lon))
		#map=str(r(lat+"+"+lon))
		main=str("| IP:  "+tip+" \n| Status: "+status+"\n| country: "+cntry+"\n| Country Code: "+cntrycd+"\n| Region: "+region+"\n| Region Name: "+regionnam+"\n| City: "+city+"\n| ZIP: "+zip+"\n| Lat: "+lat+"\n| Lon: "+lon+"\n| Timezone: "+timezone+"\n| ISP: "+isp+"\n| Org: "+org+"\n| AS: "+ass+" \n| Map: "+map)
		print(main)
	
	except:
		pass
	
	input(blue+"\n\n       Press Enter To Back Previous Menu ")


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t           """+blue+"""[★] IP Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Track Your Own IP\n\t\t2. Track Your Victim IP\n\t\t3. Get a Website IP\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	if chose=="1":
		print(yellow+"\n\n")
		ipt()

	elif chose=="2":
		
		ip=input(rosy+"Enter Target IP: ")
		print(yellow+"\n\n")
		ipt(ip)

	elif chose=="3":
		os.system('clear')
		wb=input(rosy+"\nEnter Target Website: "+red)
		ip=socket.gethostbyname(wb)
		print(yellow+"\nYour Website IP is: "+ip)
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	elif chose=="00":
		break
=======
# Coded by Cracker
# CRACKER911181  

 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBzb2NrZXQKaW1wb3J0IHRpbWUsb3Msc3lzCgoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCgoKZGVmIGlwdChpcHA9IiIpOgoJdHJ5OgoJCWFwaT1yZXF1ZXN0cy5nZXQoImh0dHA6Ly9pcC1hcGkuY29tL2pzb24vIitpcHApLmpzb24oKQoJCgkJdGlwPXN0cihhcGlbInF1ZXJ5Il0pCgkJc3RhdHVzPXN0cihhcGlbInN0YXR1cyJdKQoJCWNudHJ5PXN0cihhcGlbImNvdW50cnkiXSkKCQljbnRyeWNkPXN0cihhcGlbImNvdW50cnlDb2RlIl0pCgkJcmVnaW9uPXN0cihhcGlbInJlZ2lvbiJdKQoJCXJlZ2lvbm5hbT1zdHIoYXBpWyJyZWdpb25OYW1lIl0pCgkJY2l0eT1zdHIoYXBpWyJjaXR5Il0pCgkJemlwPXN0cihhcGlbInppcCJdKQoJCWxhdD1zdHIoYXBpWyJ'
love = 'fLKDvKFxXPDyfo249p3ElXTSjnIfvoT9hVy0cPtxWqTygMKciozH9p3ElXTSjnIfvqTygMKciozHvKFxXPDycp3N9p3ElXTSjnIfvnKAjVy0cPtxWo3WaCKA0pvuupTyoVz9lMlWqXDbWPJSmpm1mqUVbLKOcJlWuplWqXDbWPJ1upQ1mqUVbVzu0qUOmBv8iq3q3Yzqio2qfMF5wo20ioJSjpl9joTSwMF8vX3A0pvufLKDcXlVeVvgmqUVboT9hXFxXPDxwoJSjCKA0pvulXTkuqPfvXlVeoT9hXFxXPDygLJyhCKA0pvtvsPOWHQbtVPVeqTyjXlVtKT58VSA0LKE1pmbtVvgmqTS0qKZeVykhsPOwo3IhqUW5BvNvX2AhqUW5XlWpoajtD291oaElrFOQo2EyBvNvX2AhqUW5L2DeVykhsPOFMJqco246VPVepzIanJ9hXlWpoajtHzIanJ9hVR5uoJH6VPVepzIanJ9hozSgXlWpoajtD2y0rGbtVvgwnKE5XlWpoajtJxyDBvNvX3ccpPfvKT58VRkuqQbtVvgfLKDeVykhsPOZo246VPVeoT9hXlWpoajtITygMKciozH6VPVeqTygMKciozHeVykhsPOWH1N6VPVenKAjXlWpoajtG3WaBvNvX29lMlfvKT58VRSGBvNvX2SmplfvVSkhsPOALKN6VPVeoJSjXDbWPKOlnJ50XT1unJ4cPtxXPJI4L2IjqQbXPDyjLKAmPtxXPJyhpUI0XTWfqJHeVykhKT4tVP'
god = 'AgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgoKd2hpbGUgVHJ1ZToKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQoYmx1ZStmIiIiCiAgIF9fX18gICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgXwogIC8gX19ffF8gX18gX18gXyAgX19ffCB8IF9fX19fIF8gX18gICB8XyAgIF98X18gICBfX18gfCB8CiAiIiIrYmx1ZSsiIiJ8IHwgICB8ICdfXy8gX2AgfC8gX198IHwvIC8gXyBcICdfX3xfX19ffCB8LyBfIFwgLyBfIFx8IHwKICIiIitwZXN0KyIiInwgfF9fX3wgfCB8IChffCB8IChfX3wgICA8ICBfXy8gfCB8X19fX198IHwgKF8pIHwgKF8pIHwgfAogIFxfX19ffF98ICBcX18sX3xcX19ffF98XF9cX19ffF98ICAgICAgIHxffFxfX18vIFxfX18vfF98XG5cbiAiIiIrZ3JlZW4rIiIiICAgICAgICAgICAgIENyYWNrIFlvdXIgV29ybGQsIElmIFlvdSBDYW5cblxuXHQgICAgICAgICAgICIiIitibHVlKyIiIlvimIVdIElQIFRvb2wgW+KYhV0gXG4iIiIrZ3JlZW4rIiIiID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09P'
destiny = 'G09CG09CFVvVvgwo2kiqKWiMzLcPtxXPtywnT9mMG1mqUVbnJ5jqKDbpTImqPfvKT5pqSk0ZF4tIUWuL2ftJJ91pvOCq24tFIOpoyk0KUDlYvOHpzSwnlOMo3IlVSMcL3EcoFOWHSkhKUEpqQZhVRqyqPOuVSqyLaAcqTHtFIOpoyk0KUDvX3WyMPfvZQNhVRWuL2ftIT8tFT9gMFVepz9mrFfvKT5poxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWnJLtL2uip2H9CFVkVwbXPDyjpzyhqPu5MJkfo3peVykhKT4vXDbWPJyjqPtcPtbWMJkcMvOwnT9mMG09VwVvBtbWPDbWPJyjCJyhpUI0XUWip3xeVxIhqTIlVSEupzqyqPOWHQbtVvxXPDyjpzyhqPu5MJkfo3peVykhKT4vXDbWPJyjqPucpPxXPtyyoTyzVTAbo3AyCG0vZlV6PtxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWq2V9nJ5jqKDbpz9mrFfvKT5SoaEypvOHLKWaMKDtI2Ivp2y0MGbtVvglMJDcPtxWnKN9p29wn2I0YzqyqTuip3EvrJ5uoJHbq2VcPtxWpUWcoaDbrJIfoT93XlWpoyyiqKVtI2Ivp2y0MFOWHPOcpmbtVvgcpPxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWMJkcMvOwnT9mMG09VwNjVwbXPDyvpzIunj=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

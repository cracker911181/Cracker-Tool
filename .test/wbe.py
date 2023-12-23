
# Coded by Cracker
# CRACKER911181
 



<<<<<<< HEAD
import requests,socket
import os,sys,time



#text colour()
#creator: CRACKER911181

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



def dns_er():
	domain=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	link=str("http://api.hackertarget.com/dnslookup/?q="+domain)
	dns=requests.get(link).text
	os.system('clear')
	print("\n\n\t    "+green+"Your DNS Result\n\n"+yellow+dns)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")

def dns():
	try:
		dns_er()
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


##########################

def hostsearcher():
	domain=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	link=str("https://api.hackertarget.com/hostsearch/?q="+domain)
	dns=requests.get(link).text
	os.system('clear')
	print("\n\n\t    "+green+"Your HOST FINDER Result\n\n"+yellow+dns)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")
	

def httpfind():
	try:
		hostsearcher()
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


############################

def httpheader():
	domain=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	link=str("https://api.hackertarget.com/httpheaders/?q="+domain)
	dns=requests.get(link).text
	os.system('clear')
	print("\n\n\t    "+green+"Your HTTP HEADER Result\n\n"+yellow+dns)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")


def httphead():
	try:
		httpheader()
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
		
#############################


def extractor():
	web=str(input(rosy+"\nEnter Your Link without 'https' or 'http': "))
	try:
		data=requests.get("https://api.hackertarget.com/pagelinks/?q="+web).text
		os.system('clear')
		print("\n\n\t    "+green+"Your Extract Link Result\n\n"+yellow+data)
	
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


#############################


def shared_d():
	web=str(input(rosy+"\nEnter Your Domain (eg: 'google.com'): "))
	try:
		data=requests.get("https://api.hackertarget.com/findshareddns/?q="+web).text
		os.system('clear')
		print("\n\n\t    "+green+"Your Shared DNS Result\n\n"+yellow+data)
	
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


#############################



def open_port():
	web=str(input(rosy+"\nEnter Your IP (eg: '11.11.123.456'): "))
	try:
		data=requests.get("https://internetdb.shodan.io/"+web).json()
		os.system('clear')
		try:
			print("\n\n\t    "+green+"Your Open Port Scanned Result\n\n"+yellow+"Cpes: "+str(data["cpes"])+"\nHostname: "+str(data["hostnames"])+"\nIP: "+str(data["ip"])+"\nPort: "+str(data["ports"])+"\nTags: "+str(data["tags"])+"\nVuln: "+str(data['vulns']))
		except:
			print("\n\n\t    "+green+"Your Open Port Scanned Result\n\n"+yellow+str(data["detail"]))
	
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\tCheck Your Internet Connection")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	except:
		print(red+"\n\n\tSomething went Wrong")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")


#############################








while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] WEB Tool [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.DNS Lookup\n\t\t2.HOST Finder\n\t\t3.HTTP header\n\t\t4.Open Port Scanner\n\t\t5.Shared DNS Finder\n\t\t6.Link Extractor\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		dns()
	
	elif chose=="2":
		httpfind()
	
	elif chose=="3":
		httphead()
	
	elif chose=="4":
		open_port()
	
	elif chose=="5":
		shared_d()
	
	elif chose=="6":
		extractor()
		
	elif chose=="00":
		break



# https://api.hackertarget.com/hostsearch/?q=google.com


# https://api.hackertarget.com/httpheaders/?q=google.com

# https://api.hackertarget.com/zonetransfer/?q=google.com

### link extracktor
# https://api.hackertarget.com/pagelinks/?q=google.com
=======
import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLHNvY2tldAppbXBvcnQgb3Msc3lzLHRpbWUKCgoKI3RleHQgY29sb3VyKCkKI2NyZWF0b3I6IENSQUNLRVI5MTExODEKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCgoKZGVmIGRuc19lcigpOgoJZG9tYWluPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgRG9tYWluIChlZzogJ2dvb2dsZS5jb20nKTogIikpCglsaW5rPXN0cigiaHR0cDovL2FwaS5oYWNrZXJ0YXJnZXQuY29tL2Ruc2xvb2t1cC8/cT0iK2RvbWFpbikKCWRucz1yZXF1ZXN0cy5nZXQobGluaykudGV4dAoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludCgiXG5cblx0ICAgICIrZ3JlZW4rIllvdXIgRE5TIFJlc3VsdFxuXG4iK3llbGxvdytkbnMpCglpbnB1dChibHVlKyJcblxuICAgICAgIFByZXNzIEVudGVyIFRvIEJhY2sgUHJldmlvdXMgTWVudSAiKQoKZGVmIGRucygpOgoJdHJ5OgoJCWRuc19lcigpCglleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXJyb3I6CgkJcHJpbnQocmVkKyJcblxuXHRDaGVjayBZb3VyIEludGVybmV0IENvbm5lY3Rpb24iKQoJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCglleGNlcHQ6CgkJcHJpbnQocmVkKyJcblxuXHRTb21ldGhpbmcgd2VudCBXcm9uZyIpCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKZGVmIGhvc3RzZWFyY2hlcigpOgoJZG9tYWluPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgRG9tYWluIChlZzogJ2dvb2dsZS5jb20nKTogIikpCglsaW5rPXN0cigiaHR0cHM6Ly9hcGkuaGFja2VydGFyZ2V0LmNvbS9ob3N0c2VhcmNoLz9xPSIrZG9tYWluKQoJZG5zPXJlcXVlc3RzLmdldChsaW5rKS50ZXh0Cglvcy5zeXN0ZW0oJ2NsZWFyJykKCXByaW50KCJcblxuXHQgICAgIitncmVlbisiWW91ciBIT1NUIEZJTkRFUiBSZXN1bHRcblxuIit5ZWxsb3crZG5zKQoJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCQoKZGVmIGh0dHBmaW5kKCk6Cgl0cnk6CgkJaG9zdHNlYXJjaGVyKCkKCWV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoKCQlwcmludChyZWQrIlxuXG5cdENoZWNrIFlvdXIgSW50ZXJuZXQgQ29ubmVjdGlvbiIpCgkJaW5wdXQoYmx1ZSsiXG5cbi'
love = 'NtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPJI4L2IjqQbXPDyjpzyhqPulMJDeVykhKT5pqSAioJI0nTyhMlO3MJ50VSqlo25aVvxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbXPvZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZXPzEyMvObqUEjnTIuMTIlXPx6Ptyxo21unJ49p3ElXTyhpUI0XUWip3xeVykhEJ50MKVtJJ91pvORo21unJ4tXTIaBvNaM29iM2kyYzAioFpcBvNvXFxXPJkcozf9p3ElXPWbqUEjpmbiY2SjnF5bLJAeMKW0LKWaMKDhL29gY2u0qUObMJSxMKWmYm9kCFVeMT9gLJyhXDbWMT5mCKWypKIyp3EmYzqyqPufnJ5eXF50MKu0Ptyipl5mrKA0MJ0bW2AfMJSlWlxXPKOlnJ50XPWpoykhKUDtVPNtVvgapzIyovfvJJ91pvOVISEDVRuSDHESHvOFMKA1oUEpoykhVvg5MJkfo3peMT5mXDbWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPtcxMJLtnUE0pTuyLJDbXGbXPKElrGbXPDybqUEjnTIuMTIlXPxXPJI4L2IjqPOlMKS1MKA0pl5yrTAypUEco25mYxAioz5yL3Eco25SpaWipwbXPDyjpzyhqPulMJDeVykhKT5pqRAbMJAeVSyiqKVtFJ50MKWhMKDtD29hozIwqTyiovVcPtxWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPJI4L2IjqQbXPDyjpzyhqPulMJDeVykhKT5pqSAioJI0nTyhMlO3MJ50VSqlo25aVvxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWPDbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbXPzEyMvOyrUElLJA0o3VbXGbXPKqyLw1mqUVbnJ5jqKDbpz9mrFfvKT5SoaEypvOMo3IlVRkcozftq2y0nT91qPNanUE0pUZaVT9lVPqbqUEjWmbtVvxcPty0pax6PtxWMTS0LG1lMKS1MKA0pl5aMKDbVzu0qUOmBv8iLKOcYzuuL2gypaEupzqyqP5wo20ipTSaMJkcozgmYm9kCFVeq2IvXF50MKu0PtxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWpUWcoaDbVykhKT5pqPNtVPNvX2qlMJIhXlWMo3IlVRI4qUWuL3DtGTyhnlOFMKA1oUEpoykhVvg5MJkfo3peMTS0LFxXPDbWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtbWMKuwMKO0VUWypKIyp3EmYzI4L2IjqTyioaZhD29hozIwqTyioxIlpz9lBtbWPKOlnJ50XUWyMPfvKT5poyk0D2uyL2ftJJ91pvOWoaEypz5yqPOQo25hMJA0nJ9hVvxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWMKuwMKO0BtbWPKOlnJ50XUWyMPfvKT5poyk0H29gMKEbnJ5aVUqyoaDtI3WiozpvXDbWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3Zt'
god = 'RW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCgpkZWYgc2hhcmVkX2QoKToKCXdlYj1zdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb3VyIERvbWFpbiAoZWc6ICdnb29nbGUuY29tJyk6ICIpKQoJdHJ5OgoJCWRhdGE9cmVxdWVzdHMuZ2V0KCJodHRwczovL2FwaS5oYWNrZXJ0YXJnZXQuY29tL2ZpbmRzaGFyZWRkbnMvP3E9Iit3ZWIpLnRleHQKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludCgiXG5cblx0ICAgICIrZ3JlZW4rIllvdXIgU2hhcmVkIEROUyBSZXN1bHRcblxuIit5ZWxsb3crZGF0YSkKCQoJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgoJZXhjZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuQ29ubmVjdGlvbkVycm9yOgoJCXByaW50KHJlZCsiXG5cblx0Q2hlY2sgWW91ciBJbnRlcm5ldCBDb25uZWN0aW9uIikKCQlpbnB1dChibHVlKyJcblxuICAgICAgIFByZXNzIEVudGVyIFRvIEJhY2sgUHJldmlvdXMgTWVudSAiKQoJZXhjZXB0OgoJCXByaW50KHJlZCsiXG5cblx0U29tZXRoaW5nIHdlbnQgV3JvbmciKQoJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCgoKZGVmIG9wZW5fcG9ydCgpOgoJd2ViPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgSVAgKGVnOiAnMTEuMTEuMTIzLjQ1NicpOiAiKSkKCXRyeToKCQlkYXRhPXJlcXVlc3RzLmdldCgiaHR0cHM6Ly9pbnRlcm5ldGRiLnNob2Rhbi5pby8iK3dlYikuanNvbigpCgkJb3Muc3lzdGVtKCdjbGVhcicpCgkJdHJ5OgoJCQlwcmludCgiXG5cblx0ICAgICIrZ3JlZW4rIllvdXIgT3BlbiBQb3J0IFNjYW5uZWQgUmVzdWx0XG5cbiIreWVsbG93KyJDcGVzOiAiK3N0cihkYXRhWyJjcGVzIl0pKyJcbkhvc3RuYW1lOiAiK3N0cihkYXRhWyJob3N0bmFtZXMiXSkrIlxuSVA6ICIrc3RyKGRhdGFbImlwIl0pKyJcblBvcnQ6ICIrc3RyKGRhdGFbInBvcnRzIl0pKyJcblRhZ3M6ICIrc3RyKGRhdGFbInRhZ3MiXSkrIlxuVnVsbjogIitzdHIoZGF0YVsndnVsbnMnXSkpCgkJZXhjZXB0OgoJCQlwcmludCgiXG5cblx0ICAgICIrZ3JlZW4rIllvdXIgT3BlbiBQb3J0IFNjYW5uZWQgUmVzdWx0XG5cbiIreWVsbG93K3N0cihkYXRhWyJkZXRhaWwiXSkpCgkKCQlpbnB1dChibHVlKyJcblxuICAgICAgIFByZXNzIEVudGVyIFRvIEJhY2sgUHJldmlvdXMgTWVudSAiKQoKCWV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoKCQlwcmludChyZWQrIlxuXG5cdENoZWNrIFlvdXIgSW50ZXJuZXQgQ29ubmVjdGlvbiIpCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYW'
destiny = 'AeVSOlMKMco3ImVR1yoaHtVvxXPJI4L2IjqQbXPDyjpzyhqPulMJDeVykhKT5pqSAioJI0nTyhMlO3MJ50VSqlo25aVvxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbXPvZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwPtbXPtbXPtbXq2ucoTHtIUW1MGbXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tI0IPVSEio2jtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqQRhER5GVRkio2g1pSkhKUEpqQVhFR9GIPOTnJ5xMKWpoyk0KUDmYxuHISNtnTIuMTIlKT5pqSk0AP5CpTIhVSOipaDtH2Auoz5ypykhKUEpqQHhH2uupzIxVREBHlOTnJ5xMKWpoyk0KUD2YxkcozftEKu0pzSwqT9lKT5pqSk0VvglMJDeVwNjYxWuL2ftIT8tFT9gMIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWnJLtL2uip2H9CFVkVwbXPDyxoaZbXDbWPtyyoTyzVTAbo3AyCG0vZvV6PtxWnUE0pTMcozDbXDbWPtyyoTyzVTAbo3AyCG0vZlV6PtxWnUE0pTuyLJDbXDbWPtyyoTyzVTAbo3AyCG0vAPV6PtxWo3Oyoy9jo3W0XPxXPDbWMJkcMvOwnT9mMG09VwHvBtbWPKAbLKWyMS9xXPxXPDbWMJkcMvOwnT9mMG09VwLvBtbWPJI4qUWuL3EipvtcPtxWPtyyoTyzVTAbo3AyCG0vZQNvBtbWPJWlMJSePtbXPvZtnUE0pUZ6Yl9upTxhnTSwn2IlqTSlM2I0YzAioF9bo3A0p2IupzAbYm9kCJqio2qfMF5wo20XPtbwVTu0qUOmBv8iLKOcYzuuL2gypaEupzqyqP5wo20inUE0pTuyLJEypaZiC3R9M29iM2kyYzAioDbXVlObqUEjpmbiY2SjnF5bLJAeMKW0LKWaMKDhL29gY3ciozI0pzShp2Mypv8/pG1ao29aoTHhL29gPtbwVlZtoTyhnlOyrUElLJAeqT9lPvZtnUE0pUZ6Yl9upTxhnTSwn2IlqTSlM2I0YzAioF9jLJqyoTyhn3ZiC3R9M29iM2kyYzAioD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))


>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

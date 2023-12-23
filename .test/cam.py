
# Coded by Cracker
# CRACKER911181


<<<<<<< HEAD
import requests,re,os,time,sys


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest


def cc():
	os.system("clear")
	print(yellow+"""

 1| United States           2| Japan
 3| Italy                   4| Korea
 5| France                  6| Germany
 7| Taiwan                  8| Russian Federation
 9| United Kingdom         10| Netherlands
11| Czech Republic         12| Turkey
13| Austria                14| Switzerland
15| Spain                  16| Canada
17| Sweden                 18| Israel
19| Iran                   20| Poland
21| India                  22| Norway
23| Romania                24| Viet Nam
25| Belgium                26| Brazil
27| Bulgaria               28| Indonesia
29| Denmark                30| Argentina
31| Mexico                 32| Finland
33| China                  34| Chile
35| South Africa           36| Slovakia
37| Hungary                38| Ireland
39| Egypt                  40| Thailand
41| Ukraine                42| Serbia
43| Hong Kong              44| Greece
45| Portugal               46| Latvia
47| Singapore              48| Iceland
49| Malaysia               50| Colombia
51| Tunisia                52| Estonia
53| Dominican Republic     54| Sloveania
55| Ecuador                56| Lithuania
57| Palestinian            58| New Zealand
59| Bangladeh              60| Panama
61| Moldova                62| Nicaragua
63| Malta                  64| Trinidad And Tobago
65| Soudi Arabia           66| Croatia
67| Cyprus                 68| Pakistan
69| United Arab Emirates   70| Kazakhstan
71| Kuwait                 72| Venezuela
73| Georgia                74| Montenegro
75| El Salvador            76| Luxembourg
77| Curacao                78| Puerto Rico
79| Costa Rica             80| Belarus
81| Albania                82| Liechtenstein
83| Bosnia And Herzegovia  84| Paraguay
85| Philippines            86| Faroe Islands
87| Guatemala              88| Nepal
89| Peru                   90| Uruguay
""")

	
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	
	country=["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
	                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
	                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
	                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
	                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
	                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
	                 "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
	                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
	                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
	                 "-"]
	
	chose=int(input(rosy+"\nEnter Your Option: "+green))
	
	cntry=country[chose-1]
	
	
	url1=str("https://www.insecam.org/en/bycountry/"+str(cntry))
	
	page=requests.get(url1,headers=headers).text
	
	pgnmbr=re.findall(r'pagenavigator\("\?page=", (\d+)', page)[0]
	os.system("clear")
	for page in range(int(pgnmbr)):
		
		url=str("https://www.insecam.org/en/bycountry/"+cntry+"/?page="+str(page))
		
		res=requests.get(url,headers=headers).text
	
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res)
		
		for ip in find_ip:
			print(ip)

def main():
	try:
		cc()
		input(blue+"\n\nPress Enter To Back Previous Menu ")
	
	except requests.exceptions.ConnectionError:
		print(red+"\n\n\t\tCheck Your Internet Connection")
		input(blue+"\n\nPress Enter To Back Previous Menu ")
	
	except IndexError:
		pass
	
	except:
		print(red+"\n\n\t\tSomething went Wrong")
		input(blue+"\n\nPress Enter To Back Previous Menu ")

while True:
	os.system("clear")
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] CCTV Hack [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Public CCTV Hack\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	if chose=="1":
		main()
	elif chose=="00":
		break
	
	
=======
import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLHJlLG9zLHRpbWUsc3lzCgoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCmRlZiBjYygpOgoJb3Muc3lzdGVtKCJjbGVhciIpCglwcmludCh5ZWxsb3crIiIiCgogMXwgVW5pdGVkIFN0YXRlcyAgICAgICAgICAgMnwgSmFwYW4KIDN8IEl0YWx5ICAgICAgICAgICAgICAgICAgIDR8IEtvcmVhCiA1fCBGcmFuY2UgICAgICAgICAgICAgICAgICA2fCBHZXJtYW55CiA3fCBUYWl3YW4gICAgICAgICAgICAgICAgICA4fCBSdXNzaWFuIEZlZGVyYXRpb24KIDl8IFVuaXRlZCBLaW5nZG9tICAgICAgICAgMTB8IE5ldGhlcmxhbmRzCjExfCBDemVjaCBSZXB1YmxpYyAgICAgICAgIDEyfCBUdXJrZXkKMTN8IEF1c3RyaWEgICAgICAgICAgICAgICAgMTR8IFN3aXR6ZXJsYW5kCjE1fCBTcGFpbiAgICAgICAgICAgICAgICAgIDE2fCBDYW5hZGEKMTd8IFN3ZWRlbiAgICAgICAgICAgICAgICAgMTh8IElzcmFlbAoxOXwgSXJhbiAgICAgICAgICAgICAgICAgICAyMHwgUG9sYW5kCjIxfCBJbmRpYSAgICAgICAgICAgICAgICAgIDIyfCBOb3J3YXkKMjN8IFJvbWFuaWEgICAgICAgICAgICAgICAgMjR8IFZpZXQgTmFtCjI1fCBCZWxnaXVtICAgICAgICAgICAgICAgIDI2fCBCcmF6aWwKMjd8IEJ1bGdhcmlhICAgICAgICAgICAgICAgMjh8IEluZG9uZXNpYQoyOXwgRGVubWFyayAgICAgICAgICAgICAgICAzMHwgQXJnZW50aW5hCjMxfCBNZXhpY28gICAgICAgICAgICAgICAgIDMyfCBGaW5sYW5kCjMzfCBDaGluYSAgICAgICAgICAgICAgICAgIDM0fCBDaGlsZQozNXwgU291dGggQWZyaWNhICAgICAgICAgICAzNnwgU2xvdmFraWEKMzd8IEh1bmdhcnkgICAgICAgICAgICAgICAgMzh8IElyZWxhbmQKMzl8IEVneXB0ICAgICAgICAgICAgICAgICAgNDB8IFRoYWlsYW5kCjQxfCBVa3JhaW5lICAgICAgICAgICAgICAgIDQyfCBTZXJiaWEKNDN8IEhvbmcgS29uZyAgICAgICAg'
love = 'VPNtVPNtAQE8VRqlMJIwMDb0AKjtHT9lqUIaLJjtVPNtVPNtVPNtVPNtVPN0AajtGTS0qzyuPwD3sPOGnJ5aLKOipzHtVPNtVPNtVPNtVPNtVQD4sPOWL2IfLJ5xPwD5sPOALJkurKAcLFNtVPNtVPNtVPNtVPNtVQHjsPOQo2kioJWcLDb1ZKjtIUIhnKAcLFNtVPNtVPNtVPNtVPNtVPN1ZajtEKA0o25cLDb1Z3jtET9gnJ5cL2ShVSWypUIvoTywVPNtVPN1AUjtH2kiqzIuozyuPwH1sPOSL3IuMT9lVPNtVPNtVPNtVPNtVPNtVQH2sPOZnKEbqJShnJRXAGq8VSOuoTImqTyhnJShVPNtVPNtVPNtVPNtAGu8VR5yqlOnMJSfLJ5xPwH5sPOPLJ5aoTSxMJttVPNtVPNtVPNtVPNtVQLjsPODLJ5uoJRXAwS8VR1ioTEiqzRtVPNtVPNtVPNtVPNtVPNtAwW8VR5cL2SlLJq1LDb2Z3jtGJSfqTRtVPNtVPNtVPNtVPNtVPNtVPN2AUjtIUWcozyxLJDtDJ5xVSEiLzSaojb2AKjtH291MTxtDKWuLzyuVPNtVPNtVPNtVPN2AajtD3WiLKEcLDb2A3jtD3yjpaImVPNtVPNtVPNtVPNtVPNtVPN2BUjtHTSenKA0LJ4XAwy8VSIhnKEyMPOOpzSvVRIgnKWuqTImVPNtAmO8VRgurzSenUA0LJ4XAmS8VRg1q2ScqPNtVPNtVPNtVPNtVPNtVPNtAmW8VSMyozI6qJIfLDb3Z3jtE2IipzqcLFNtVPNtVPNtVPNtVPNtVPN3AUjtGJ9hqTIhMJqlojb3AKjtEJjtH2SfqzSxo3VtVPNtVPNtVPNtVPN3AajtGUI4MJ1vo3IlMjb3A3jtD3IlLJAuolNtVPNtVPNtVPNtVPNtVPN3BUjtHUIypaEiVSWcL28XAmy8VRAip3EuVSWcL2RtVPNtVPNtVPNtVPNtBQO8VRWyoTSlqKZXBQS8VRSfLzShnJRtVPNtVPNtVPNtVPNtVPNtBQW8VRkcMJAbqTIhp3EynJ4XBQA8VRWip25cLFOOozDtFTIlrzIao3McLFNtBQE8VSOupzSaqJS5Pwt1sPODnTyfnKOjnJ5yplNtVPNtVPNtVPNtVQt2sPOTLKWiMFOWp2kuozEmPwt3sPOUqJS0MJ1uoTRtVPNtVPNtVPNtVPNtVQt4sPOBMKOuoNb4BKjtHTIlqFNtVPNtVPNtVPNtVPNtVPNtVPN5ZUjtIKW1M3IurDbvVvVcPtbWPtybMJSxMKWmVQ0trlWIp2IlYHSaMJ50VwbtVx1irzyfoTRiAF4jVPuLZGR7VRkcoaI4VTx2BQL7VUW2BwL4YwNcVRqyL2giYmVjZGNjZGNkVRMcpzIzo3tiAwthZPW9PtxXPJAiqJ50pax9JlWIHlVfVPWXHPVfVPWWIPVfVPWYHvVfVPWTHvVfVPWREFVfVPWHIlVfVPWFIFVfVPWUDvVfVPWBGPVfPtxtVPNtVPNt'
god = 'ICAgICAgICAgICJDWiIsICJUUiIsICJBVCIsICJDSCIsICJFUyIsICJDQSIsICJTRSIsICJJTCIsICJQTCIsICJJUiIsCgkgICAgICAgICAgICAgICAgICJOTyIsICJSTyIsICJJTiIsICJWTiIsICJCRSIsICJCUiIsICJCRyIsICJJRCIsICJESyIsICJBUiIsCgkgICAgICAgICAgICAgICAgICJNWCIsICJGSSIsICJDTiIsICJDTCIsICJaQSIsICJTSyIsICJIVSIsICJJRSIsICJFRyIsICJUSCIsCgkgICAgICAgICAgICAgICAgICJVQSIsICJSUyIsICJISyIsICJHUiIsICJQVCIsICJMViIsICJTRyIsICJJUyIsICJNWSIsICJDTyIsCgkgICAgICAgICAgICAgICAgICJUTiIsICJFRSIsICJETyIsICJTSSIsICJFQyIsICJMVCIsICJQUyIsICJOWiIsICJCRCIsICJQQSIsCgkgICAgICAgICAgICAgICAgICJNRCIsICJOSSIsICJNVCIsICJJVCIsICJTQSIsICJIUiIsICJDWSIsICJQSyIsICJBRSIsICJLWiIsCgkgICAgICAgICAgICAgICAgICJLVyIsICJWRSIsICJHRSIsICJNRSIsICJTViIsICJMVSIsICJDVyIsICJQUiIsICJDUiIsICJCWSIsCgkgICAgICAgICAgICAgICAgICJBTCIsICJMSSIsICJCQSIsICJQWSIsICJQSCIsICJGTyIsICJHVCIsICJOUCIsICJQRSIsICJVWSIsCgkgICAgICAgICAgICAgICAgICItIl0KCQoJY2hvc2U9aW50KGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBPcHRpb246ICIrZ3JlZW4pKQoJCgljbnRyeT1jb3VudHJ5W2Nob3NlLTFdCgkKCQoJdXJsMT1zdHIoImh0dHBzOi8vd3d3Lmluc2VjYW0ub3JnL2VuL2J5Y291bnRyeS8iK3N0cihjbnRyeSkpCgkKCXBhZ2U9cmVxdWVzdHMuZ2V0KHVybDEsaGVhZGVycz1oZWFkZXJzKS50ZXh0CgkKCXBnbm1icj1yZS5maW5kYWxsKHIncGFnZW5hdmlnYXRvclwoIlw/cGFnZT0iLCAoXGQrKScsIHBhZ2UpWzBdCglvcy5zeXN0ZW0oImNsZWFyIikKCWZvciBwYWdlIGluIHJhbmdlKGludChwZ25tYnIpKToKCQkKCQl1cmw9c3RyKCJodHRwczovL3d3dy5pbnNlY2FtLm9yZy9lbi9ieWNvdW50cnkvIitjbnRyeSsiLz9wYWdlPSIrc3RyKHBhZ2UpKQoJCQoJCXJlcz1yZXF1ZXN0cy5nZXQodXJsLGhlYWRlcnM9aGVhZGVycykudGV4dAoJCgkJZmluZF9pcCA9IHJlLmZpbmRhbGwociJodHRwOi8vXGQrLlxkKy5cZCsuXGQrOlxkKyIsIHJlcykKCQkK'
destiny = 'PDyzo3VtnKNtnJ4tMzyhMS9cpQbXPDxWpUWcoaDbnKNcPtcxMJLtoJScovtcBtbWqUW5BtbWPJAwXPxXPDycoaO1qPuvoUIyXlWpoykhHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtxXPJI4L2IjqPOlMKS1MKA0pl5yrTAypUEco25mYxAioz5yL3Eco25SpaWipwbXPDyjpzyhqPulMJDeVykhKT5pqSk0D2uyL2ftJJ91pvOWoaEypz5yqPOQo25hMJA0nJ9hVvxXPDycoaO1qPuvoUIyXlWpoykhHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtxXPJI4L2IjqPOWozEyrRIlpz9lBtbWPKOup3ZXPDbWMKuwMKO0BtbWPKOlnJ50XUWyMPfvKT5poyk0KUEGo21yqTucozptq2IhqPOKpz9hMlVcPtxWnJ5jqKDbLzk1MFfvKT5poyOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbXq2ucoTHtIUW1MGbXPJ9mYaA5p3EyoFtvL2kyLKVvXDbWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tD0AHIvOVLJAeVSivzVIqVSkhVvVvX2qlMJIhXlVvVvN9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0vVvVeL29fo3Ilo2MzXDbWPtbWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKUEpqQRhVSO1LzkcLlOQD1EJVRuuL2gpoyk0KUDvX3WyMPfvZQNhVRWuL2ftIT8tFT9gMFVepz9mrFfvKT5poxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWnJLtL2uip2H9CFVkVwbXPDygLJyhXPxXPJIfnJLtL2uip2H9CFVjZPV6PtxWLaWyLJfXPDbW'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969


# Coded by Cracker
# CRACKER911181


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
	
	
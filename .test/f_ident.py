# Coded by Cracker
# CRACKER911181



<<<<<<< HEAD

import requests,json,os,time


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest




def fake_ident():
	data=requests.get("https://randomuser.me/api").json()
	
	
	fname=str(data["results"][0]["name"]["first"]
	)
	lname=str(data["results"][0]["name"]["last"])
	gender=str(data["results"][0]["gender"])
	location=str(str(data["results"][0]["location"]["street"]["number"])+","+str(data["results"][0]["location"]["street"]["name"])+","+str(data["results"][0]["location"]["city"])+","+str(data["results"][0]["location"]["state"])+","+str(data["results"][0]["location"]["country"]))
	postcode=str(data["results"][0]["location"]["postcode"])
	email=str(data["results"][0]["email"])
	user=str(data["results"][0]["login"]["username"])
	pwd=str(data["results"][0]["login"]["password"])
	age=str(data["results"][0]["dob"]["age"])
	pic=str(data["results"][0]["picture"]["large"])
	
	os.system("clear")
	main=(green+"\n\nFirst Name: "+fname+"\nLast Name: "+lname+"\nGender: "+gender+"\nAge: "+age+"\nPicture: "+pic+"\nEmail: "+email+"\nUsername: "+user+"\nPassword: "+pwd+"\nPost Code: "+postcode+"\nLocation: "+location)
	
	print(main)



while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t    """+blue+"""[★] Fake Identity Generator [★] \n"""+green+""" ========================================================="""+colouroff)
	

	chose=str(input(pest+"\n\t\t1. Identity Generate\n\t\t"+red+"00. Back To Home"+rosy+"\n\nEnter Your Option: "))
	
	
	if chose=="00":
		break

	elif chose=="1":
		fake_ident()
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
=======
import base64, codecs
magic = 'CmltcG9ydCByZXF1ZXN0cyxqc29uLG9zLHRpbWUKCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKCgpkZWYgZmFrZV9pZGVudCgpOgoJZGF0YT1yZXF1ZXN0cy5nZXQoImh0dHBzOi8vcmFuZG9tdXNlci5tZS9hcGkiKS5qc29uKCkKCQoJCglmbmFtZT1zdHIoZGF0YVsicmVzdWx0cyJdWzBdWyJuYW1lIl1bImZpcnN0Il0KCSkKCWxuYW1lPXN0cihkYXRhWyJyZXN1bHRzIl1bMF1bIm5hbWUiXVsibGFzdCJdKQoJZ2VuZGVyPXN0cihkYXRhWyJyZXN1bHRzIl1bMF1bImdlbmRlciJdKQoJbG9jYXRpb249c3RyKHN0cihkYXRhWyJyZXN1bHRzIl1bMF1bImxvY2F0aW9uIl1bInN0cmVldCJdWyJudW1i'
love = 'MKVvKFxeVvjvX3A0pvuxLKEuJlWlMKA1oUEmVy1oZS1oVzkiL2S0nJ9hVy1oVaA0pzIyqPWqJlWhLJ1yVy0cXlVfVvgmqUVbMTS0LIfvpzImqJk0plWqJmOqJlWfo2AuqTyiovWqJlWwnKE5Vy0cXlVfVvgmqUVbMTS0LIfvpzImqJk0plWqJmOqJlWfo2AuqTyiovWqJlWmqTS0MFWqXFfvYPVep3ElXTEuqTSoVaWyp3IfqUZvKIfjKIfvoT9wLKEco24vKIfvL291oaElrFWqXFxXPKOip3Ewo2EyCKA0pvuxLKEuJlWlMKA1oUEmVy1oZS1oVzkiL2S0nJ9hVy1oVaOip3Ewo2EyVy0cPtyyoJScoQ1mqUVbMTS0LIfvpzImqJk0plWqJmOqJlWyoJScoPWqXDbWqKAypw1mqUVbMTS0LIfvpzImqJk0plWqJmOqJlWfo2qcovWqJlW1p2IlozSgMFWqXDbWpUqxCKA0pvuxLKEuJlWlMKA1oUEmVy1oZS1oVzkiM2yhVy1oVaOup3A3o3WxVy0cPtyuM2H9p3ElXTEuqTSoVaWyp3IfqUZvKIfjKIfvMT9vVy1oVzSaMFWqXDbWpTywCKA0pvuxLKEuJlWlMKA1oUEmVy1oZS1oVaOcL3E1pzHvKIfvoTSlM2HvKFxXPDbWo3Zhp3ymqTIgXPWwoTIupvVc'
god = 'CgltYWluPShncmVlbisiXG5cbkZpcnN0IE5hbWU6ICIrZm5hbWUrIlxuTGFzdCBOYW1lOiAiK2xuYW1lKyJcbkdlbmRlcjogIitnZW5kZXIrIlxuQWdlOiAiK2FnZSsiXG5QaWN0dXJlOiAiK3BpYysiXG5FbWFpbDogIitlbWFpbCsiXG5Vc2VybmFtZTogIit1c2VyKyJcblBhc3N3b3JkOiAiK3B3ZCsiXG5Qb3N0IENvZGU6ICIrcG9zdGNvZGUrIlxuTG9jYXRpb246ICIrbG9jYXRpb24pCgkKCXByaW50KG1haW4pCgoKCndoaWxlIFRydWU6Cglvcy5zeXN0ZW0oJ2NsZWFyJykKCXByaW50KGJsdWUrZiIiIgogICBfX19fICAgICAgICAgICAgICAgIF8gICAgICAgICAgICAgICAgX19fX18gICAgICAgICAgIF8KICAvIF9fX3xfIF9fIF9fIF8gIF9fX3wgfCBfX19fXyBfIF9fICAgfF8gICBffF9fICAgX19fIHwgfAogIiIiK2JsdWUrIiIifCB8ICAgfCAnX18vIF9gIHwvIF9ffCB8LyAvIF8gXCAnX198X19fX3wgfC8gXyBcIC8gXyBcfCB8CiAiIiIrcGVzdCsiIiJ8IHxfX198IHwgfCAoX3wgfCAoX198ICAgPCAgX18vIHwgfF9f'
destiny = 'K19ssPO8VPusXFO8VPusXFO8VUjXVPOpK19sK3kssPNtKS9sYS98KS9sK3kssSksKS9sK3kssPNtVPNtVPO8K3kpK19sYlOpK19sY3kssSkhKT4tVvVvX2qlMJIhXlVvVvNtVPNtVPNtVPNtVPOQpzSwnlOMo3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0VPNtVPVvVvgvoUIyXlVvVyivzVIqVRMun2HtFJEyoaEcqUxtE2IhMKWuqT9lVSivzVIqVSkhVvVvX2qlMJIhXlVvVvN9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0vVvVeL29fo3Ilo2MzXDbWPtbWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKUEpqQRhVRyxMJ50nKE5VRqyozIlLKEyKT5pqSk0VvglMJDeVwNjYvOPLJAeVSEiVRuioJHvX3Wip3xeVykhKT5SoaEypvOMo3IlVR9jqTyiowbtVvxcPtxXPDbWnJLtL2uip2H9CFVjZPV6PtxWLaWyLJfXPtyyoTyzVTAbo3AyCG0vZFV6PtxWMzSeMI9cMTIhqPtcPtxWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

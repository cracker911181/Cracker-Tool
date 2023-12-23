
# Coded by Cracker
# CRACKER911181
 

import base64, codecs
<<<<<<< HEAD
from telethon.sync import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telegram.ext import Updater,CommandHandler 
import os,sys,time
import random





#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest




def allsms():
	print(rosy+"\n[+] Login Your Telegram Account\n")
	with TelegramClient("name", 760985, "30d734ab9a2c2712b0fcf953936d5a88") as client:
	    result = client(functions.contacts.GetContactsRequest(
	        hash=0
	    ))
	    x=str(result.stringify())
	#    print(x)
	    oo=open("contact.txt","w")
	    oo.write(x)
	    oo.close()
	text=str(input(rosy+"\n\nEnter Your Message: "))
	oo=open("contact.txt","r")
	o=oo.read()
	t=str(o)
	tt=t.find("[")
	ttt=t.find("]")
	v=(t[tt:ttt])
	sp=v.split("\n")
	for x in sp:
		k=x.find("user_id=")
		g=x.find(",")
		b=(x[k:g])
		k=(b[8:18])
		if k=="":
			continue
		else:
			d=(int(k))
			with TelegramClient('name', 7609852, "30d734ab9a2c2712b0fcf953936d5a88") as client:
				client.send_message(d, text)
				print(red+"\tMessage To",d)
	
	print(green+"\n\n\t\tDone")
	time.sleep(7)
#############################

def bomb():
	print(rosy+"\n[+] Login Your Telegram Account\n")
	with TelegramClient("name",7609852,"30d734ab9a2c2712b0fcf953936d5a88") as client:
		vic=str(input(rosy+"\nEnter Your Victim: "+red))
		amnt=int(input(rosy+"Enter Sending Amount: "+red))
		print("\n\n")
		for i in range(amnt):
			ms=random.randint(111111,999999)
			mss=str(ms)
			msg="""**Login code**: """+mss+""". Do **not** give this code to anyone, even if they say they are from Telegram!
	
	This code can be used to log in to your Telegram account. We never ask it for anything else.
	
	If you didn't request this code by trying to log in on another device, simply ignore this message."""
			
			client.send_message(vic,msg)
			print(red+"\t\tSms Send")
		print(green+"\n\n\t\tDone")
		time.sleep(7)
		os.system('clear')

#############################



def bot():
	while True:
		token=str(input(green+"\n\nEnter Your Bot Token: "))
		if token=="":
			print(red+"\n\n\t Token Error")
		else:
			break
	cmd1=str(input(rosy+"\nEnter Your 1st Command: "))
	txt1=str(input("Enter Your Reply: "))
	
	cmd2=str(input("\nEnter Your 2nd Command: "))
	txt2=str(input("Enter Your Reply: "))
	
	cmd3=str(input("\nEnter Your 3rd Command: "))
	txt3=str(input("Enter Your Reply: "))
	
	cmd4=str(input("\nEnter Your 4th Command: "))
	txt4=str(input("Enter Your Reply: "))
	
	cmd5=str(input("\nEnter Your 5th Command: "))
	txt5=str(input("Enter Your Reply: "))
	
	
	
	if cmd1=="":
		cmd1="cracker"
	if cmd2=="":
		cmd2="cracker"
	if cmd3=="":
		cmd3="cracker"
	if cmd4=="":
		cmd4="cracker"
	if cmd5=="":
		cmd5="cracker"
	
	
	if txt1=="":
		txt1="cracker"
	if txt2=="":
		txt2="cracker"
	if txt3=="":
		txt3="cracker"
	if txt4=="":
		txt4="cracker"
	if txt5=="":
		txt5="cracker"
	
	
	
	############################
	
	
	def text1(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt1)
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt1)
	
	
	#######################
	
	def text2(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt2)
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt2)
	
	########################
	
	def text3(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt3)
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt3)
	
	
	#######################
	
	def text4(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt4)
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt4)
	
	
	#########################
	
	
	def text5(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt5)
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text=txt5)
	
	
	###########################
	
	def start(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text='Hey! Welcomeߤ頠 ')
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text='Hey! Welcomeߤ頠 ')
	
	
	#############################
	
	def stop(update, context):
		try:
			context.bot.send_message(chat_id=update.effective_chat.id,text='Good Byeߘ䠠 ')
		except:
			context.bot.send_message(chat_id=update.effective_chat.id,text="Good Byeߘ䠠 ")
	
	
	#############################
	
	
	def main():
		updater = Updater(token)
		
		dp = updater.dispatcher
		
		
		#######
		
		dp.add_handler(CommandHandler('start',start))
		
		dp.add_handler(CommandHandler('stop',stop))
		
		dp.add_handler(CommandHandler(cmd1,text1))
		
		dp.add_handler(CommandHandler(cmd2,text2))
		
		dp.add_handler(CommandHandler(cmd3,text3))
		
		dp.add_handler(CommandHandler(cmd4,text4))
		
		dp.add_handler(CommandHandler(cmd5,text5))
		
		print(green+"\n\n\t\tStarted")
		########
		
		updater.start_polling()
		
		updater.idle()
	
	try:
		main()
	except:
		main()


while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Telegram Kit [★] \n"""+green+""" ========================================================="""+colouroff)
	chose=str(input(pest+"\n\n\t\t1.Telegram Bombing\n\t\t2.All Telegram Contact Sms Send\n\t\t3.Bot Command Genaretor\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		try:
			bomb()
		except:
			pass
	elif chose=="2":
		try:
			allsms()
		except:
			pass
	elif chose=="3":
		try:
			bot()
		except:
			pass
	elif chose=="00":
		break
=======
magic = 'ZnJvbSB0ZWxldGhvbi5zeW5jIGltcG9ydCBUZWxlZ3JhbUNsaWVudCwgZXZlbnRzCmZyb20gdGVsZXRob24uc3luYyBpbXBvcnQgVGVsZWdyYW1DbGllbnQKZnJvbSB0ZWxldGhvbiBpbXBvcnQgZnVuY3Rpb25zLCB0eXBlcwpmcm9tIHRlbGVncmFtLmV4dCBpbXBvcnQgVXBkYXRlcixDb21tYW5kSGFuZGxlciAKaW1wb3J0IG9zLHN5cyx0aW1lCmltcG9ydCByYW5kb20KCgoKCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKCgpkZWYgYWxsc21zKCk6CglwcmludChyb3N5KyJcblsrXSBMb2dpbiBZb3VyIFRlbGVncmFtIEFjY291bnRcbiIpCgl3aXRoIFRlbGVncmFtQ2xpZW50KCJuYW1lIiwgNzYwOTg1LCAiMzBkNzM0YWI5YTJjMjcxMmIwZmNmOTUzOTM2ZDVhODgiKSBhcyBjbGllbnQ6CgkgICAgcmVzdWx0ID0gY2xpZW50KGZ1bmN0aW9ucy5jb250YWN0cy5HZXRDb250YWN0c1JlcXVlc3QoCgkgICAgICAgIGhhc2g9MAoJICAgICkpCgkgICAgeD1zdHIocmVzdWx0LnN0cmluZ2lmeSgpKQoJIyAgICBwcmludCh4KQoJICAgIG9vPW9wZW4oImNvbnRhY3QudHh0IiwidyIpCgkgICAgb28ud3JpdGUoeCkKCSAgICBvby5jbG9zZSgpCgl0ZXh0PXN0cihpbnB1dChyb3N5KyJcblxuRW50ZXIgWW91ciBNZXNzYWdlOiAiKSkKCW9vPW9wZW4oImNvbnRhY3QudHh0IiwiciIpCglvPW9vLnJlYWQoKQoJdD1zdHIobykKCXR0PXQuZmluZCgiWyIpCgl0dHQ9dC5maW5kKCJdIikKCXY9KHRbdHQ6dHR0XSkKCXNwPXYuc3BsaXQoIlxuIikKCWZvciB4IGluIHNwOgoJCWs9eC5maW5kKCJ1c2VyX2lkPSIpCgkJZz14LmZpbmQoIiwiKQoJCWI9KHhbazpnXSkKCQlrPShiWzg6MThdKQoJCWlmIGs9PSIiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCWQ9KGludChrKSkKCQkJd2l0aCBUZWxlZ3JhbUNsaWVudCgnbmFtZScsIDc2MDk4NTIsICIzMGQ3MzRhYjlhMmMyNzEyYjBmY2Y5NTM5MzZkNWE4OCIpIGFzIGNsaWVudDoKCQkJCWNsaWVudC5zZW5kX21lc3NhZ2UoZCwgdGV4dCkKCQkJCXByaW50KHJlZCsiXHRNZXNzYWdlIFRvIixkKQoJCglwcmludChncmVlbisiXG5cblx0XHREb25lIikKCXRpbWUuc2xlZXAoNykKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiBib21iKCk6CglwcmludChyb3N5KyJcblsrXSBMb2dpbiBZb3VyIFRlbGVncmFtIEFjY291bnRcbiIpCgl3aXRoIFRlbGVncmFtQ2xpZW50KCJuYW1lIiw3NjA5ODUyLCIzMGQ3MzRhYjlhMmMyNzEyYjBmY2Y5NTM5MzZkNWE4OCIpIGFzIGNsaWVudDoKCQl2aWM9c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBWaWN0aW06ICIrcmVkKSkKCQlhbW50PWludChpbnB1dChyb3N5KyJFbnRlciBTZW5kaW5nIEFtb3VudDogIityZWQpKQoJC'
love = 'KOlnJ50XPWpoykhVvxXPDyzo3VtnFOcovOlLJ5aMFuuoJ50XGbXPDxWoKZ9pzShMT9gYaWuozEcoaDbZGRkZGRkYQx5BGx5BFxXPDxWoKAmCKA0pvugplxXPDxWoKAaCFVvVvbdGT9anJ4tL29xMFbdBvNvVvVeoKAmXlVvVv4tET8tXvcho3DdXvOanKMyVUEbnKZtL29xMFO0olOuoayiozHfVTI2MJ4tnJLtqTuyrFOmLKxtqTuyrFOupzHtMaWioFOHMJkyM3WuoFRXPDbWITucplOwo2EyVTAuovOvMFO1p2IxVUEiVTkiMlOcovO0olO5o3IlVSEyoTIapzSgVTSwL291oaDhVSqyVT5yqzIlVTSmnlOcqPOzo3VtLJ55qTucozptMJkmMF4XPDbWFJLtrJ91VTEcMT4aqPOlMKS1MKA0VUEbnKZtL29xMFOvrFO0paycozptqT8toT9aVTyhVT9hVTSho3EbMKVtMTI2nJAyYPOmnJ1joUxtnJqho3WyVUEbnKZtoJImp2SaMF4vVvVXPDxWPtxWPJAfnJIhqP5mMJ5xK21yp3AuM2HbqzywYT1mMlxXPDxWpUWcoaDbpzIxXlWpqSk0H21mVSAyozDvXDbWPKOlnJ50XTqlMJIhXlWpoykhKUEpqREiozHvXDbWPKEcoJHhp2kyMKNbAlxXPDyipl5mrKA0MJ0bW2AfMJSlWlxXPvZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwPtbXPzEyMvOvo3DbXGbXPKqbnJkyVSElqJH6PtxWqT9eMJ49p3ElXTyhpUI0XTqlMJIhXlWpoykhEJ50MKVtJJ91pvOPo3DtIT9eMJ46VPVcXDbWPJyzVUEin2IhCG0vVwbXPDxWpUWcoaDbpzIxXlWpoykhKUDtIT9eMJ4tEKWlo3VvXDbWPJIfp2H6PtxWPJWlMJSePtywoJDkCKA0pvucoaO1qPulo3A5XlWpoxIhqTIlVSyiqKVtZKA0VRAioJ1uozD6VPVcXDbWqUu0ZG1mqUVbnJ5jqKDbVxIhqTIlVSyiqKVtHzIjoUx6VPVcXDbWPtywoJDlCKA0pvucoaO1qPtvKT5SoaEypvOMo3IlVQWhMPOQo21gLJ5xBvNvXFxXPKE4qQV9p3ElXTyhpUI0XPWSoaEypvOMo3IlVSWypTk5BvNvXFxXPDbWL21xZm1mqUVbnJ5jqKDbVykhEJ50MKVtJJ91pvNmpzDtD29goJShMQbtVvxcPty0rUDmCKA0pvucoaO1qPtvEJ50MKVtJJ91pvOFMKOfrGbtVvxcPtxXPJAgMQD9p3ElXTyhpUI0XPWpoxIhqTIlVSyiqKVtAUEbVRAioJ1uozD6VPVcXDbWqUu0AQ1mqUVbnJ5jqKDbVxIhqTIlVSyiqKVtHzIjoUx6VPVcXDbWPtywoJD1CKA0pvucoaO1qPtvKT5SoaEypvOMo3IlVQI0nPOQo21gLJ5xBvNvXFxXPKE4qQH9p3ElXTyhpUI0XPWSoaEypvOMo3IlVSWypTk5BvNvXFxXPDbWPtxXPJyzVTAgMQR9CFVvBtbWPJAgMQR9VzAlLJAeMKVvPtycMvOwoJDlCG0vVwbXPDywoJDlCFWwpzSwn2IlVtbWnJLtL21xZm09VvV6PtxWL21xZm0vL3WuL2gypvVXPJyzVTAgMQD9CFVvBtbWPJAgMQD9VzAlLJAeMKVvPtycMvOwoJD1CG0vVwbXPDywoJD1CFWwpzSwn2IlVtbWPtxXPJyzVUE4qQR9CFVvBtbWPKE4qQR9VzAlLJAeMKVvPtycMvO0rUDlCG0vVwbXPDy0rUDlCFWwpzSwn2IlVtbWnJLtqUu0Zm09VvV6PtxWqUu0Zm0vL3WuL2gypvVXPJyzVUE4qQD9CFVvBtbWPKE4qQD9VzAlLJAeMKVvPtycMvO0rUD1CG0vVwbXPDy0rUD1CFWwpzSwn2IlVtbWPtxXPDbWVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbWPtxXPJEyMvO0MKu0ZFu1pTEuqTHfVTAioa'
god = 'RleHQpOgoJCXRyeToKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0MSkKCQlleGNlcHQ6CgkJCWNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPXVwZGF0ZS5lZmZlY3RpdmVfY2hhdC5pZCx0ZXh0PXR4dDEpCgkKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHRleHQyKHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD10eHQyKQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0MikKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgkKCWRlZiB0ZXh0Myh1cGRhdGUsIGNvbnRleHQpOgoJCXRyeToKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0MykKCQlleGNlcHQ6CgkJCWNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPXVwZGF0ZS5lZmZlY3RpdmVfY2hhdC5pZCx0ZXh0PXR4dDMpCgkKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHRleHQ0KHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD10eHQ0KQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0NCkKCQoJCgkjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgkKCQoJZGVmIHRleHQ1KHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD10eHQ1KQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0NSkKCQoJCgkjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHN0YXJ0KHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD0nSGV5ISBXZWxjb21l8J+kqSAgICcpCgkJZXhjZXB0OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD0nSGV5ISBXZWxjb21l8J+kqSAgICcpCgkKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHN0b3AodXBkYXRlLCBjb250ZXh0KToKCQl0cnk6CgkJCWNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPXVwZGF0ZS5lZmZlY3RpdmVfY2hhdC5pZCx0ZXh0PSdHb29kIEJ5ZfCfmLQgICAnKQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

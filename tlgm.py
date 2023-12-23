
# Coded by Cracker
# CRACKER911181
 

import base64, codecs
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
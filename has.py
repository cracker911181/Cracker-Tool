# Coded by Cracker
# CRACKER911181
 



import hashlib
import sys,time,os,sys


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest

def main():
	import base64
	fl=open(".md.txt","r")
	fil=fl.read()
	filer=fil.encode('utf-8')
	filee=base64.b64decode(filer)
	file=str(filee.decode('utf-8'))
	sp=file.split("\n")
	
	############
	vcc=0
	for has in sp:
		
		funcer=func[0]
		hash=has.encode('utf-8')
		hasher=hashlib.new(funcer,hash)
		hashed=hasher.hexdigest()
		
		if hashed==inp:
			print(blue+"\n\n\tYour Password Cracked: \n \t   "+red+has)
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
			continue
			
		elif vcc==(len(sp))-1:
			print(red+"\n\n\tYour Password Not Match To Worldlist ")
			input(blue+"\n\n       Press Enter To Back Previous Menu ")
		vcc=vcc+1
		
		
	

while True:
	funcr=["md5","sha1","sha224","sha256","sha384","sha512","sha3-224","sha3-256","sha3-384","sha3-512","blake2b","ripemd160","whirlpool"]
	
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t         """+blue+"""[★] Has Cracker [★] \n"""+green+""" ========================================================="""+colouroff)
	chose=str(input(pest+"\n\t1. Crack MD5         2. Crack SHA1   \n\t3. Crack SHA224      4. Crack SHA256\n\t5. Crack SHA384      6. Crack SHA512\n\t7. Crack SHA3-224    8. Crack SHA3-256\n\t9. Crack SHA3-384    10.Crack SHA3-512\n\t11.Crack BLAKE2B     12.Crack RIPEMD160 \n\t13.Crack WHIRLPOOL   "+red+"00. Back To Home\n\n"+rosy+"Enter Your Has Tyle: "))
	
	
	func=[ ]
	
	if chose=="00":
		break
	
	if chose=='1':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[0]
		func.append(real)
	
	if chose=='2':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[1]
		func.append(real)
	
	
	if chose=='3':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[2]
		func.append(real)
	
	if chose=='4':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[3]
		func.append(real)
	
	if chose=='5':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[4]
		func.append(real)
	
	if chose=='6':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[5]
		func.append(real)
	
	if chose=='7':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[6]
		func.append(real)
	
	if chose=='8':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[7]
		func.append(real)
	
	if chose=='9':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[8]
		func.append(real)
	
	if chose=='10':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[9]
		func.append(real)
	
	if chose=='11':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[10]
		func.append(real)
	
	if chose=='12':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[11]
		func.append(real)
	
	if chose=='13':
		inp=str(input("\nEnter Target Hashed Code: "))
		real=funcr[12]
		func.append(real)
	
	
	if chose=="00":
		break
	
	else:
		pass
#		print()
#		continue
		
	################
	try:
		main()
	except:
		pass
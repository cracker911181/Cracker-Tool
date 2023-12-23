# Coded by Cracker 
# CRACKER911181



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
	
	print(pest+"""	1.base16-harmonic16-dark
	2.smyck
	3.base16-embers-light
	4.base16-solarized-light
	5.base16-railscasts-dark
	6.base16-londontube-light
	7.base16-ashes-dark
	8.base16-solarized-dark
	9.base16-atelierheath-light
	10.base16-twilight-dark
	11.rydgel
	12.base16-twilight-light
	13.white-on-black
	14.base16-google-light
	15.base16-greenscreen-dark
	16.base16-tomorrow-dark
	17.base16-brewer-light
	18.base16-default-light
	19.base16-flat-dark
	20.base16-londontube-dark
	21.base16-atelierdune-dark
	22.base16-isotope-light
	23.base16-grayscale-dark
	24.base16-3024-dark
	25.base16-codeschool-light
	26.base16-ashes-light
	27.base16-codeschool-dark
	28.base16-grayscale-light
	29.gotham
	30.zenburn
	31.base16-atelierforest-light
	32.base16-shapeshifter-light
	33.base16-google-dark
	34.base16-eighties-dark
	35.base16-flat-light
	36.base16-eighties-light
	37.base16-apathy-dark
	38.base16-atelierseaside-dark
	39.base16-railscasts-light
	40.base16-brewer-dark
	41.base16-atelierlakeside-dark
	42.base16-bright-light
	43.neon
	44.base16-chalk-dark
	45.base16-atelierdune-light
	46.base16-paraiso-dark
	47.wild-cherry
	48.base16-atelierheath-dark
	49.base16-bright-dark
	50.base16-atelierlakeside-light
	51.base16-3024-light
	52.base16-chalk-light
	53.base16-marrakesh-light
	54.nancy
	55.base16-summerfruit-dark
	56.tomorrow-night
	57.base16-greenscreen-light
	58.base16-paraiso-light
	59.nord
	60.base16-atelierforest-dark
	61.base16-bespin-dark
	62.base16-ocean-light
	63.base16-atelierseaside-light
	64.gruvbox-dark
	65.base16-materia
	66.gnometerm
	67.base16-ocean-dark
	68.base16-mocha-dark
	69.black-on-white
	70.base16-marrakesh-dark
	71.base16-harmonic16-light
	72.base16-bespin-light
	73.base16-monokai-light
	74.base16-monokai-dark
	75.base16-mocha-light
	76.material
	77.base16-isotope-dark
	78.base16-colors-dark
	79.base16-tomorrow-light
	80.base16-shapeshifter-dark
	81.base16-summerfruit-light
	82.base16-default-dark
	83.solarized-dark
	84.dracula
	85.base16-colors-light
	86.solarized-light
	87.base16-apathy-light
	88.gruvbox-light
	89.base16-embers-dark
	"""+green+"""90.Reset Color""")
	
	chose=str(input(rosy+"\n\nEnter Your Color: "))
	
	
	if chose=="90":
		os.system("rm -rf /data/data/com.termux/files/home/.termux/colors.properties")
			
	else:

		open("/data/data/com.termux/files/home/Cracker-Tool/.ctermux/color/"+chose+".properties","r")
		os.system("cp /data/data/com.termux/files/home/Cracker-Tool/.ctermux/color/"+chose+".properties /data/data/com.termux/files/home/.termux")
		os.system("mv /data/data/com.termux/files/home/.termux/"+chose+".properties /data/data/com.termux/files/home/.termux/colors.properties")


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

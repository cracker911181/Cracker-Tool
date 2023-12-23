# Coded by Cracker 
# CRACKER911181



<<<<<<< HEAD
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
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUsc3lzCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgpkZWYgY29sb3IoKToKCQoJcHJpbnQocGVzdCsiIiIJMS5iYXNlMTYtaGFybW9uaWMxNi1kYXJrCgkyLnNteWNrCgkzLmJhc2UxNi1lbWJlcnMtbGlnaHQKCTQuYmFzZTE2LXNvbGFyaXplZC1saWdodAoJNS5iYXNlMTYtcmFpbHNjYXN0cy1kYXJrCgk2LmJhc2UxNi1sb25kb250dWJlLWxpZ2h0Cgk3LmJhc2UxNi1hc2hlcy1kYXJrCgk4LmJhc2UxNi1zb2xhcml6ZWQtZGFyawoJOS5iYXNlMTYtYXRlbGllcmhlYXRoLWxpZ2h0CgkxMC5iYXNlMTYtdHdpbGlnaHQtZGFyawoJMTEucnlkZ2VsCgkxMi5iYXNlMTYtdHdpbGlnaHQtbGlnaHQKCTEzLndoaXRlLW9uLWJsYWNrCgkxNC5iYXNlMTYtZ29vZ2xlLWxpZ2h0CgkxNS5iYXNlMTYtZ3JlZW5zY3JlZW4tZGFyawoJMTYuYmFzZTE2LXRvbW9ycm93LWRhcmsKCTE3LmJhc2UxNi1icmV3ZXItbGlnaHQKCTE4LmJhc2UxNi1kZWZhdWx0LWxpZ2h0CgkxOS5iYXNlMTYtZmxhdC1kYXJrCgkyMC5iYXNlMTYtbG9uZG9udHViZS1kYXJrCgkyMS5iYXNlMTYtYXRlbGllcmR1bmUtZGFyawoJMjIuYmFzZTE2LWlzb3RvcGUtbGlnaHQKCTIzLm'
love = 'Wup2HkAv1apzS5p2AuoTHgMTSlnjbWZwDhLzSmMGR2YGZjZwDgMTSlnjbWZwHhLzSmMGR2YJAiMTImL2uio2jgoTyanUDXPGV2YzWup2HkAv1up2uypl1fnJqbqNbWZwphLzSmMGR2YJAiMTImL2uio2jgMTSlnjbWZwthLzSmMGR2YJqlLKymL2SfMF1fnJqbqNbWZwxhM290nTSgPtxmZP56MJ5vqKWhPtxmZF5vLKAyZGLgLKEyoTyypzMipzImqP1fnJqbqNbWZmVhLzSmMGR2YKAbLKOyp2ucMaEypv1fnJqbqNbWZmZhLzSmMGR2YJqio2qfMF1xLKWePtxmAP5vLKAyZGLgMJyanUEcMKZgMTSlnjbWZmHhLzSmMGR2YJMfLKDgoTyanUDXPGZ2YzWup2HkAv1ynJqbqTyypl1fnJqbqNbWZmphLzSmMGR2YJSjLKEbrF1xLKWePtxmBP5vLKAyZGLgLKEyoTyypaAyLKAcMTHgMTSlnjbWZmxhLzSmMGR2YKWunJkmL2SmqUZgoTyanUDXPGDjYzWup2HkAv1vpzI3MKVgMTSlnjbWAQRhLzSmMGR2YJS0MJkcMKWfLJgyp2yxMF1xLKWePtx0Zv5vLKAyZGLgLaWcM2u0YJkcM2u0Ptx0Zl5hMJ9hPtx0AP5vLKAyZGLgL2uuoTfgMTSlnjbWAQHhLzSmMGR2YJS0MJkcMKWxqJ5yYJkcM2u0Ptx0Av5vLKAyZGLgpTSlLJymol1xLKWePtx0Al53nJkxYJAbMKWlrDbWAQthLzSmMGR2YJS0MJkcMKWbMJS0nP1xLKWePtx0BF5vLKAyZGLgLaWcM2u0YJEupzfXPGHjYzWup2HkAv1uqTIfnJIloTSeMKAcMTHgoTyanUDXPGHkYzWup2HkAv0mZQV0YJkcM2u0Ptx1Zv5vLKAyZGLgL2uuoTfgoTyanUDXPGHmYzWup2HkAv1gLKWlLJgyp2tgoTyanUDXPGH0Yz5uozA5Ptx1AF5vLKAyZGLgp3IgoJIlMaW1nKDgMTSlnjbW'
god = 'NTYudG9tb3Jyb3ctbmlnaHQKCTU3LmJhc2UxNi1ncmVlbnNjcmVlbi1saWdodAoJNTguYmFzZTE2LXBhcmFpc28tbGlnaHQKCTU5Lm5vcmQKCTYwLmJhc2UxNi1hdGVsaWVyZm9yZXN0LWRhcmsKCTYxLmJhc2UxNi1iZXNwaW4tZGFyawoJNjIuYmFzZTE2LW9jZWFuLWxpZ2h0Cgk2My5iYXNlMTYtYXRlbGllcnNlYXNpZGUtbGlnaHQKCTY0LmdydXZib3gtZGFyawoJNjUuYmFzZTE2LW1hdGVyaWEKCTY2Lmdub21ldGVybQoJNjcuYmFzZTE2LW9jZWFuLWRhcmsKCTY4LmJhc2UxNi1tb2NoYS1kYXJrCgk2OS5ibGFjay1vbi13aGl0ZQoJNzAuYmFzZTE2LW1hcnJha2VzaC1kYXJrCgk3MS5iYXNlMTYtaGFybW9uaWMxNi1saWdodAoJNzIuYmFzZTE2LWJlc3Bpbi1saWdodAoJNzMuYmFzZTE2LW1vbm9rYWktbGlnaHQKCTc0LmJhc2UxNi1tb25va2FpLWRhcmsKCTc1LmJhc2UxNi1tb2NoYS1saWdodAoJNzYubWF0ZXJpYWwKCTc3LmJhc2UxNi1pc290b3BlLWRhcmsKCTc4LmJhc2UxNi1jb2xvcnMtZGFyawoJNzkuYmFzZTE2LXRvbW9ycm93LWxpZ2h0Cgk4MC5iYXNlMTYtc2hhcGVzaGlmdGVyLWRhcmsKCTgxLmJhc2UxNi1zdW1tZXJmcnVpdC1saWdodAoJODIuYmFzZTE2LWRlZmF1bHQtZGFyawoJODMuc29sYXJpemVkLWRhcmsKCTg0LmRyYWN1bGEKCTg1LmJhc2UxNi1jb2xvcnMtbGlnaHQKCTg2LnNvbGFyaXplZC1saWdodAoJODcuYmFzZTE2LWFwYXRoeS1saWdodAoJODguZ3J1dmJveC1saWdodAoJODkuYmFzZTE2LWVtYmVycy1kYXJrCgkiIiIrZ3JlZW4rIiIiOTAuUmVzZXQgQ2'
destiny = '9fo3VvVvVcPtxXPJAbo3AyCKA0pvucoaO1qPulo3A5XlWpoykhEJ50MKVtJJ91pvOQo2kipwbtVvxcPtxXPDbWnJLtL2uip2H9CFV5ZPV6PtxWo3Zhp3ymqTIgXPWloFNgpzLtY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY2uioJHiYaEypz11rP9wo2kipaZhpUWipTIlqTyyplVcPtxWPDbWMJkmMGbXPtxWo3OyovtvY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY2uioJHiD3WuL2gypv1Ho29fYl5wqTIloKI4Y2AioT9lYlVeL2uip2HeVv5jpz9jMKW0nJImVvjvpvVcPtxWo3Zhp3ymqTIgXPWwpPNiMTS0LF9xLKEuY2AioF50MKWgqKtiMzyfMKZinT9gMF9QpzSwn2IlYIEio2jiYzA0MKWgqKtiL29fo3ViVvgwnT9mMFfvYaOlo3OypaEcMKZtY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY2uioJHiYaEypz11rPVcPtxWo3Zhp3ymqTIgXPWgqvNiMTS0LF9xLKEuY2AioF50MKWgqKtiMzyfMKZinT9gMF8hqTIloKI4YlVeL2uip2HeVv5jpz9jMKW0nJImVP9xLKEuY2EuqTRiL29gYaEypz11rP9znJkypl9bo21yYl50MKWgqKtiL29fo3WmYaOlo3OypaEcMKZvXDbXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bVzAfMJSlVvxXPKElrGbXPDywo2kipvtcPtxWpUWcoaDbrJIfoT93XlWpoykhKUEpqREiozHvXDbWPKEcoJHhp2kyMKNbAFxXPDyvpzIunjbWMKuwMKO0VRMcoTIBo3ETo3IhMRIlpz9lBtbWPDbWPKOlnJ50XUWyMPfvKT5poyk0FJ52LJkcMPOQo2kipvOBqJ1vMKVvXDbWPKEcoJHhp2kyMKNbZvxXPDxXPDyjLKAmPtyyrTAypUDtHTIloJymp2yioxIlpz9lBtbWPKOup3ZW'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

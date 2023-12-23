import random,sys,logging

logging.basicConfig(level=logging.INFO)

def main(files,string):
	s=open(files).read()
	z=[]
	for i in s:
		z.append(ord(i))
	pea=[]
	for i in z:
		pea.append(string.replace("'","").replace('"','')*i)
	file="""



d={};exec("".join([chr(len(i)) for i in d]))
	""".format(pea)
	open(files.replace(".py","enc.py"),"w").write(file)


try:
	main(sys.argv[1],sys.argv[2])
except:
	print()
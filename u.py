import os

os.system("rm -rf $HOME/Cracker-Tool")

os.system("git clone https://github.com/cracker911181/Cracker-Tool")

os.system("cd Cracker-Tool")
try:
	os.system("python cracker-main.py")
except:
	print()

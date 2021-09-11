import os

os.system("rm -rf $HOME/Cracker-Tool")

os.system("git clone https://github.com/cracker911181/Cracker-Tool")

os.system("cd $HOME/Cracker-Tool")
try:
	os.system("python $HOME/Cracker-Tool/cracker-main.py")
except:
	print()

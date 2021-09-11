import os
os.system("apt update")
os.system("apt upgrade -y")
os.system("pkg install git -y")
os.system("pkg install python -y")

os.system("rm -rf $HOME/Cracker-Tool")

os.system("git clone https://github.com/cracker911181/Cracker-Tool")

os.system("cd Cracker-Tool")

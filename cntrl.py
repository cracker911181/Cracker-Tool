import os
os.system('clear')
os.system('sh requirement.sh')
os.system('rm requirement.sh')
os.system('rm -rf __pycache__')
exec(open('lg.py','r').read())

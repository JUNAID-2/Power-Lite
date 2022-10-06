#coding:utf-8
from platform import uname
from os import path,system,chmod
from sys import argv
try:
    if argv[1].lower()=="reset":
        system("rm -rf *")
        system('curl -L https://raw.githubusercontent.com/Junaid-2/Junaid/main/Lite.py.py -o Lite.py')
        system('python Lite.py')
except:
    pass
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\n\033[1;32mCongratulations! Your Device Support This Tools\033[1;37m')
else:
    exit("\033[1;31mSystem Not Support This Tools\033[1;37m")
while True:
        if path.isfile("dz.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/Junaid-2/Data/main/Lite.so -o dz.so")
import asad
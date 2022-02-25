import os,sys,time,requests,re,json,random
from random import randrange as rg
from getpass import getpass
os.system('clear')
print ("\033[94m  ╔═══════╗\033[94m")
print ("\033[94m  ║       ║\033[94m       \033[31m[\033[31m\033[33m SUBSCRIBE CHANNEL Ammar Execute\033[33m\033[31m ] \033[31m")
print ("\033[94m╔═══════════╗\033[94m")
print ("\033[94m║\033[94m \033[32mL O G I N \033[32m\033[94m║\033[94m   \033[31m[\033[33m \033[37mCreator\033[37m\033[37m :\033[37m\033[32m AmmarBN\033[32m\033[31m ] \033[31m")
print ("\033[94m║\033[94m \033[37m  TOOLS\033[37m \033[94m  ║")
print ("\033[94m╚═══════════╝\033[94m")
print ('')
print (' \033[94m[\033[94m\033[33m*\033[33m\033[94m]\033[94m\033[37m\033[31m[ \033[31m\033[37mLogin Username dan pasword download link dibawa\033[37m\033[31m ]\033[31m')
print (' \033[94m[\033[94m\033[33m*\033[33m\033[94m]\033[94m\033[37m\033[31m[\033[31m\033[37m Link\033[37m \033[31m]\033[31m\033[37m\033[33m :\033[33m \033[31m[\033[31m\033[32mbit.ly/MediaFirepaswordtxtcom\033[32m\033[31m ]\033[31m')

def login():
	os.system("python login.py")

def menu():
      while True:
           print("")
           try:
                x = str(input('\033[1;34mUsername \033[1;93m:\033[1;92m '))
                e = getpass('\033[1;36mPassword \033[1;93m:\033[1;92m ')
                print ("")
                if x=="Ammar Ganz" and e=="hdhehejwbshbahai15sg2":
                   print('[✓]\033[1;92m Token Benar')
                   time.sleep(2)
                   os.system('python main.py')
                   print('')
                   time.sleep(2)
                   break
                else:
                      print("\033[1;91m[×]\033[1;92m Token Salah")
                      time.sleep(2)
           except Exception:
                      print("\033[1;91mWrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      os.system('killall -9 com.termux')
                      print("\033[1;91m[•] Progran Dihentikan")
                      time.sleep(2)
menu()

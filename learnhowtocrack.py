import hashlib
import time
import os

GREEN = '\033[92m'
red = "\u001b[31m"

def banner():
  os.system("clear")
  print(GREEN+"coded by youhacker55")


  print(red+"""the goal of this simple script 
  to make user learn how hashing work and how attacker crack
  hashes please read the code""")
  time.sleep(2.5)
banner()


hash = input('entre the hash:')
print( """1) use rockyou.txt 
2) use your own wordlist""")
user = int(input("root@cracker:"))
if user == 1:
  wordlistpath = "rockyou.txt"
  if os.path.exists("rockyou.txt") == True:
    pass
  else:
    print(GREEN+"[+]installing rockyou for you")
    time.sleep(0.5)
    print("this may take sometime")
    time.sleep(0.5)
    os.system('curl  https://raw.githubusercontent.com/praetorian-inc/Hob0Rules/master/wordlists/rockyou.txt.gz -o rockyou.txt.gz')
    os.system("gzip -d rockyou.txt.gz")
elif user == 2:
  wordlistpath = input("entre your wordlist path:")
with open(wordlistpath,'r') as list:
  for i in list:
    x = i.rstrip('\n')
    encoding = hashlib.md5(x.encode())
    compare = encoding.hexdigest()
    if compare == hash:
      print(GREEN+"hash cracked:",x)
      break
    else:
      print(red,x,'is not the right word')

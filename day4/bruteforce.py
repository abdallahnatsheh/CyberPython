from urllib.request import urlopen
import hashlib
from termcolor import colored

hashedPassword = input("enter the hash password :") #40123e9c6273385ea69892c48c80aa6cb25b9113 : mustang
randomPassword = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt').read(),encoding='utf-8')
allPassword = randomPassword.split('\n')
#print(allPassword)


for password in allPassword:
    bytePassword = bytes(password,'utf-8')
    hashedRandomPassword = hashlib.sha1(bytePassword).hexdigest()
    if hashedPassword == hashedRandomPassword:
        print("the password is : ", password)
        break
    else:
        print("not matched", password)



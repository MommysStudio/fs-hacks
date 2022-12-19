from os import system
import os
import os.path
import time
import requests
import string
import random
import xml.etree.ElementTree as ET

system('title fs hack')

def crypt(txt):
    low = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = {'1','2','3','4','5','6','7','8','9','0'}
    specs = {'~','`','!','@','#','%','^','&','*'}
    step = 0
    final = '..:Mommy#1111 DATA Encryptor:..'
    while not step == len(txt):
        for i in low:
            if random.randint(1,5) == 1:
                final += i
        for i in specs:
            if random.randint(1,5) == 1:
                final += i
        final += '$'+txt[step]
        for i in upper:
            if random.randint(1,5) == 1:
                final += i
        for i in nums:
            if random.randint(1,5) == 1:
                final += i
        if step == 0:
            step = 1
        else:
            step += 1
    return final

#print(crypt('test'))      #encryptor example

def encrypt(txt):
    step = 0
    final = ''
    while not step == len(txt):
        if txt[step] == '$':
            final += txt[step + 1]
        if step == 0:
            step = 1
        else:
            step += 1
    return final

#print(encrypt('..:Mommy#1111 DATA Encryptor:..amvx`%*$tADI286dhijy`$eWXZ9dhinoruz@$sDNWdfgijlpw&$tAFHQTZ95'))      #decryptor example

def msg(msg,title):
    system(f'echo x=msgbox("{msg}",64,"{title}") > msg.vbs')
    time.sleep(.1)
    system('start msg.vbs')
    time.sleep(.1)
    system('del msg.vbs')
    time.sleep(.1)

#msg('xd','lol')   #message example


def copy_file(path,destination):
    system(f'xcopy "{path}" "{destination}"')

#copy_file('test\*',f'{os.environ["userprofile"]}\Documents\My Games\FarmingSimulator2011')      #copy file example

def reset_token(token):
    answer_get = requests.get(f'https://www.mommy1111.xyz/fs11/reset_token.php?key={token}')
    if answer_get.text == 'done':
        system('del key.DATA')
        msg('reseted token enter your key to enter program','fs cheats')
        startup()
    else:
        print(answer_get.text)
        exit()

def check_token(token):
    answer_get = requests.get(f'https://www.mommy1111.xyz/fs11/token_check.php?token={token}')
    if answer_get.text == 'ok':
        return True
    else:
        return False

def check_key(key):
    answer_get = requests.get(f'https://www.mommy1111.xyz/fs11/key_check.php?key={key}')
    if not answer_get.text == 'not ok':
        return answer_get.text
    else:
        msg('wrong key','fs hacks')
        print('wrong key')
        return False

def change_money_fs11():
    system('cls')
    sv = input('enter savegame that u want to hack on : ')
    amm = input('enter money ammount : ')
    save1 = ET.parse(f'{os.environ["userprofile"]}\Documents\My Games\FarmingSimulator2011\savegame{sv}\careerSavegame.XML')
    save = save1.getroot()
    save.set('money',f"{amm}")
    time.sleep(0.1)
    save1.write(f'{os.environ["userprofile"]}\Documents\My Games\FarmingSimulator2011\savegame{sv}\careerSavegame.XML')
    msg('money changed','money hack')
    fs11()

def fs11():
    system('cls')
    print('type 1 to enter money changer')
    choose = input('choose cheat : ')
    if choose == '1':
        change_money_fs11()
    else:
        msg('???????','fs11 hacks')
        fs11()


def init_menu1():
    system('cls')
    print('type 1 to enter fs 11 cheats')
    choose = input('choose fs : ')
    if choose == '1':
        fs11()
    else:
        msg('????','fs hacks')
        init_menu1()


def startup():
    system('cls')
    if os.path.isfile('key.DATA'):
        key = open('key.DATA')
        if check_token(encrypt(key.read())) == True:
            init_menu1()
        else:
            key.close()
            choose = input('wrong token do you want to reset your token? (Y/N) : ')
            if choose == 'Y' or choose == 'y':
                token = input('enter your key : ')
                reset_token(token)
                startup()
            else:
                exit
    else:
        key = input('enter your key : ')
        key_check = check_key(key)
    if not key_check == False:
        key = key_check
        msg('correct key','fs hacks')
        key1 = open('key.DATA','a+')
        key1.write(crypt(key))
        key1.close()
        init_menu1()

startup()
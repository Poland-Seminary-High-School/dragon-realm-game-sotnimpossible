import random
import time 
def displayintro():
    print('you are in a Place and theres so many freaking Dragons In it. theres two caves in front of you. one cave has a nice friendly dragon whomst will share his many Treasures with you. the other cave contains Evil Dragon whomst will eat and bite and consume thee.')
def choosecave():
    cavenumber=''
    while cavenumber!='1' and cavenumber!='2':
        print('which cave do you wanna go in (1/2)')
        cavenumber=input()
    return cavenumber
def checkcave(chosencave):
    print('you Approach the cave')
    time.sleep(2)
    print('its dark and spooky and whatnot')
    time.sleep(2)
    friendcave=random.randint(1, 2)
    if chosencave==str(friendcave):
        print('you find a huge like 12 foot tall fire dragon. he hands you a hot topic gift card.\n')
    else:
        print("you find a tiny lizard atop a pile of coins. you no longer exist and the memory of you is erased from all your loved ones' minds along with your very being. nice going bro.\n")
playagain='yes'
while playagain=='yes' or playagain=='y':
    displayintro()
    cavenumber=choosecave()
    checkcave(cavenumber)
    print('do you wanna subject yourself to that again.')
    playagain=input().lower()
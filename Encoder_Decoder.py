
import pprint as pp
import Arethmitic_Coding
from decimal import getcontext
from decimal import Decimal
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
os.system('cls')
width = os.get_terminal_size().columns
getcontext().prec=10
#Custom color print functions
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk).center(width))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk).center(width))
cprint(figlet_format('Welcome!',justify="center",width = width), 'yellow', attrs=['bold'])
while True:

    print("\033[93m Choose the desired functionality: \033[00m".center(width+10))
    print("\033[93m  -enter 0 to encode \033[00m".center(width+10))
    print("\033[93m -enter 1 to decode \033[00m".center(width+10))

    Choice=input()
    #encoding
    if Choice=='0':
        prCyan("Welcome To arethmetic Encoder!")
        prCyan('#'*100)
        msg=input('Enter The Message you want to compress:')
        mlen=len(msg)
        PTab=Arethmitic_Coding.Probability(msg)
        prCyan('#'*100)
        prYellow('Probability Table:')
        pp.pprint(PTab,width=1)
        prCyan('#'*100)
        prYellow('Coded Message:')
        prGreen(Arethmitic_Coding.encode(msg,PTab)[1])
        code=Arethmitic_Coding.encode(msg,PTab)[1]
        break
    #Decoding
    elif Choice=='1':
        prCyan("Welcome To arethmetic decoder!")
        prCyan('#'*100)
        mlen=int(input('enter how many characters in the Msg:'))
        PTab={}
        print(f'enter the chars followed by their probabilities separated by a space (ex:a 0.2) enter 0 to exit:')
        char=""
        while True:
            char=input()
            if char=='0':
                break
            PTab[char[0]]=Decimal(char[1:])
        prCyan('#'*100)
        code=Decimal(input('Enter the coded msg:'))
        prYellow('Original Message:')
        prGreen(Arethmitic_Coding.decode( code,mlen,PTab)[1])

        break
    else: 
        os.system('cls')
        prRed('wrong Functionality pls try again!')
        




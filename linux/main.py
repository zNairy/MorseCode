from MorseCode import MorseCode
from os import system
from sys import exit

__author__ = 'zNairy'
__contact__ = 'Discord: "__Nairy__#7181" ou www.github.com/zNairy'
__version__ = '1.0'

def TextEncode(string):
    morse = MorseCode()
    print(f'  "{morse.TextEncode(string)}"\n')

def TextDecode(string):
    morse = MorseCode()
    print(f'  "{morse.TextDecode(string)}"\n')

def BeepFromPlainText(string):
    morse = MorseCode()
    morse.BeepFromPlainText(string)

def BeepFromMorseCode(string):
    morse = MorseCode()
    morse.BeepFromMorseCode(string)

def main():
    print(f' Morse encode/decode by {__author__}! | Contact {__contact__} | version {__version__}')
    print(how_to_use())
    options = {
        '1': TextEncode, 
        '2': TextDecode, 
        '3': BeepFromPlainText, 
        '4': BeepFromMorseCode
        }

    question = str(input(' > '))
    system('clear')
    
    try:
        while question.strip() != '0':
            options[question](str(input(' Text: ')))
            main()
        
        exit(0)
    except KeyError:
        main()
    except KeyboardInterrupt:
        exit(0)

def how_to_use():
    return "   1 - Encode morse from simple text.\n   2 - Decode morse.\n   3 - Beeps from simple text.\n   4 - Beeps from morse code.\n   0 - leave\n"

if __name__ == '__main__':
    main()
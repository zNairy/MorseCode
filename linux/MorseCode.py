from json import loads
from Beep import MorseBeep
from time import sleep

class MorseCode(object):
    ''' Simple morse encoder and decoder '''
    def __init__(self):
        self.__Alphabet = self.OpenMorseAlphabet()
        self.runBeep = {'.': MorseBeep.RunDotBeep, '-': MorseBeep.RunTraceBeep}

    def OpenMorseAlphabet(self):
        with open('morseAlphabet.json', 'r') as file:
            morseAlphabet = loads(file.read().encode())
            file.close()
            return morseAlphabet
    
    def TextDecode(self, string):
        return ''.join(self.__Alphabet['Normal'].get(let, '') for let in string.strip().split(' '))
        
    def TextEncode(self, string):
        return ''.join(f"{self.__Alphabet['Morse'].get(let, '')} " for let in string.strip())
    
    def BeepFromPlainText(self, string):
        string = self.TextEncode(string).strip()
        
        for word in string.split():
            for let in word:
                if self.runBeep.get(let):
                    sleep(0.05)
                    self.runBeep[let]()
            
            sleep(0.3)

    def BeepFromMorseCode(self, string):
        for word in string.split():
            for let in word:
                if self.runBeep.get(let):
                    sleep(0.05)
                    self.runBeep[let]()
            
            sleep(0.3)
from os import system

class MorseBeep(object):
    ''' sound beeps for morse code class (linux)'''
    @staticmethod
    def RunTraceBeep():
        system('play -nq -t alsa synth 0.4 sine 500')

    @staticmethod
    def RunDotBeep():
        system('play -nq -t alsa synth 0.1 sine 500')
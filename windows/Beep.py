from winsound import Beep

class MorseBeep(object):
    ''' sound beeps for morse code class (windows)'''
    @staticmethod
    def RunTraceBeep():
        Beep(500, 0.4)

    @staticmethod
    def RunDotBeep():
        Beep(500, 0.1)
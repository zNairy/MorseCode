from winsound import Beep

class Beep(object):
    ''' sound beeps for morse code class (linux)'''
    @staticmethod
    def RunTraceBeep():
        Beep(500, 0.4)

    @staticmethod
    def RunDotBeep():
        Beep(500, 0.1)
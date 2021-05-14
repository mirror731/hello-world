# -*- coding: utf-8 -*-
'''set a simple alarm and return a message beep when time's up'''

import winsound, time, os

def sound():
    '''alarm the sound'''
    for i in range(2): # Number of repeats
        winsound.MessageBeep(-1) # Sound played
        time.sleep(2) # How long between beeps
        
def alarm(n):
    print(f"Alarm in {n} seconds later")
    time.sleep(n) # suspend execution for n seconds
    print("Time's up")
    sound()
    
def clock(x):
    '''
    allow user set the alarm in hour,min,sec
    '''
    if x == "1":
        set_alarm = int(input("Set your alarm in hours: "))
        t = set_alarm * 60 * 60
        alarm(t)
    elif x == "2":
        set_alarm = int(input("Set your alarm in mintues: "))
        t = set_alarm * 60
        alarm(t)
    elif x == "3":
        set_alarm = int(input("Set your alarm in seconds: "))
        t = set_alarm
        alarm(t)
    elif x == "4":
        h = int(input("Set your alarm in hours: "))
        m = int(input("Set your alarm in mintues: "))
        s = int(input("Set your alarm in seconds: "))
        t = h * 60 * 60 + m * 60 + s
        print(f"Your alarm: {h}:{m}:{s}")
        alarm(t)
    else:
        try:
            os.system("cls") # clear output for windows
            main()
        except:
            os.systme("clear") # clear output for linux or mac
            main()

def main():
    print("Choose the type of your alarm\n 1 hours only\n 2 mintues only\n 3 seconds only\n 4 complex")
    choice = input(": ")
    clock(choice)
    
if __name__ == '__main__':
    main()
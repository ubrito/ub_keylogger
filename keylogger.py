from pynput.keyboard import Listener

def capture(key):
    print(str(key))

with Listener(on_press=capture) as l:
    l.join()
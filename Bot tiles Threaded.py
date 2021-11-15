from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import threading

px = 0
py = 0

class Tile():
    def __init__(self,px,py):  
        self.x = px
        self.y = py
 
def checktile(tileob,color,reverse):
        if reverse:
            while True:
                if pyautogui.pixel(tileob.x,tileob.y) != color:
                    thread = threading.Thread(target = click, args = (tileob.x,tileob.y))
                    thread.daemon = True
                    thread.start()
                    while pyautogui.pixel(tileob.x,tileob.y) != color:
                        time.sleep(0.1)
            
        else:
            while True:
                if pyautogui.pixel(tileob.x,tileob.y) == color:
                    print("Found in " + str(tileob.x) + "," + str(tileob.y))
                    thread = threading.Thread(target = click, args = (tileob.x,tileob.y))
                    thread.daemon = True
                    thread.start()
                    break

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
print("Press Q on the color we want to snipe")
while True:
    if keyboard.read_key() == "q":
        px = position().x
        py = position().y
        color = pyautogui.pixel(px, py)
        time.sleep(0.1)
        break

tiles = int(input("How many tiles?\n"))
tilesp = []
threadlist = []
for tile in range(tiles):
    print("Press Q on tile " + str(tile))
    while True:
        if keyboard.read_key() == "q":
            px = position().x
            py = position().y
            tilesp.append(Tile(px,py))
            time.sleep(0.1)
            break

for tileob in tilesp:
    thread = threading.Thread(target = checktile, args = (tileob,color,False))
    threadlist.append(thread)


print("Hold K to snipe or J to reverse snipe! - Press P to stop the bot")
running = False
toggle = False
while True:
    if keyboard.is_pressed("p") == True:
            print("Exiting!")
            break
    if keyboard.is_pressed("l") == True:
        toggle = not toggle
        print(toggle)
        time.sleep(0.1)
    if toggle:
        if running  == False:
            for thread in threadlist:
                thread.daemon = True
                thread.start()
            running=True

    else:
        if running == True:
            for thread in threadlist:
                thread.daemon = True
                thread.start()
            running=False
        if keyboard.is_pressed("k") == True:
            for tile in tilesp:
                if pyautogui.pixel(tile.x,tile.y) == color:
                    click(tile.x,tile.y)
        if keyboard.is_pressed("j") == True:
            for tile in tilesp:
                if pyautogui.pixel(tile.x,tile.y) != color:
                    click(tile.x,tile.y)
    
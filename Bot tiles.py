from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

px = 0
py = 0

class Tile():
    def __init__(self,px,py):  
        self.x = px
        self.y = py
 

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

tiles = int(input("How many tiles?\n"))
tilesp = []
for tile in range(tiles):
    print("Press Q on tile " + str(tile))
    while True:
        if keyboard.read_key() == "q":
            px = position().x
            py = position().y
            tilesp.append(Tile(px,py))
            time.sleep(0.1)
            break
print("Press Q on the color we want to snipe")
while True:
    if keyboard.read_key() == "q":
        px = position().x
        py = position().y
        color = pyautogui.pixel(px, py)
        time.sleep(0.1)
        break
print(color)

print("Hold K to snipe or J to reverse snipe! - Press P to stop the bot")
toggle = False
while True:
    if keyboard.read_key() == "l":
        toggle = not toggle
        print(toggle)
        time.sleep(0.1)
    if toggle:
        while toggle:
            for tile in tilesp:
                if pyautogui.pixel(tile.x,tile.y) == color:
                    click(tile.x,tile.y)
            if keyboard.read_key() == "l":
                toggle = not toggle
                print(toggle)
                time.sleep(0.1)
            if keyboard.is_pressed("p") == True:
                print("Exiting!")
                break
    else:
        if keyboard.is_pressed("k") == True:
            for tile in tilesp:
                if pyautogui.pixel(tile.x,tile.y) == color:
                    click(tile.x,tile.y)
        if keyboard.is_pressed("j") == True:
            for tile in tilesp:
                if pyautogui.pixel(tile.x,tile.y) != color:
                    click(tile.x,tile.y)
    if keyboard.is_pressed("p") == True:
            print("Exiting!")
            break
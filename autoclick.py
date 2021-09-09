import pyautogui
import keyboard

x = True
while x == True:
    def shortcut():
        x = True
        while x == True:
            pyautogui.click(clicks=1, interval=0.02, button='left')

            if keyboard.is_pressed('e'):
                x = False


    if keyboard.is_pressed('1'):
        shortcut()
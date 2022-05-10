import os
import pyautogui
# from pynput.keyboard import Key, Controller

# keyboard = Controller()

text = [
    "Hello my child...",
    "I've been watching you...",
    "You have been very naughty my boy...",
    "We do not tolerate this boy...",
    "We are on our way now boy...",
    "Anyways see you later BYE!"
]

os.system("sleep 4")

for i in range(0, 6):
    os.system("sleep 4")
    pyautogui.press("enter")
    pyautogui.typewrite(text[i])

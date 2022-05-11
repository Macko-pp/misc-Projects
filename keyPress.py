import os
import pyautogui

text = [
    "Hello, my child...",
    "I'm the FBI agent youre always talking about...",
    "I've been watching you...",
    "You have been very naughty, my boy...",
    "We do not tolerate this, boy...",
    "We are on our way now, boy...",
    "Be careful, boy...",
    "Remember...",
    "We are ALWAYS watching...",
]

os.system("sleep 1")

for i in range(len(text)):
    os.system("sleep 4")
    pyautogui.press("enter")
    pyautogui.typewrite(text[i])

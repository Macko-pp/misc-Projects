from time import sleep
import os
import pyautogui as gui
from tqdm import tqdm

for i in range(0, 5):

    for i in tqdm(range(0, 300)):

        if i == 290:
            os.system("afplay '/Applications/Desktop\ Goose.app/Contents/Resources/Honk1.mp3")

        sleep(1)

    gui.click(85, 388)
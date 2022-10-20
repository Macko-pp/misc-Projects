from time import sleep
from pyautogui import click
from tqdm import tqdm
from playsound import playsound

for i in range(0, 15):
    for i in tqdm(range(0, 300)):
        if i == 290:
            playsound("/Users/maxkonietzko/Python/Bell.mp3")

        sleep(1)

    click(19, 23)
    sleep(0.5)

    for i in range(1, 9):
        click(((i + 2) * 100), 450)
        sleep(0.05)

    for i in range(1, 9):
        click(((i + 2) * 100), 464)
        sleep(0.05)

    click(1000, 518)
    sleep(1)
    click(155, 23)

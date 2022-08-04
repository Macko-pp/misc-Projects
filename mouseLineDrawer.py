import pyautogui
import os
import random

os.system("sleep 2")

ranX = random.randrange(62, 1439)
ranY = random.randrange(161, 826)

pyautogui.mouseDown(ranX, ranY)

def drawLine():
	ranX1 = random.randrange(62, 1439)
	ranY1 = random.randrange(161, 826)

	pyautogui.mouseDown()
	pyautogui.moveTo(ranX1, ranY1, 0.25)
	pyautogui.mouseUp()

for i in range(1, 50):
	drawLine()
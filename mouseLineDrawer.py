import pyautogui
import os
import random

os.system("sleep 2")

# for i in range(1, 50):
# 	ranX1 = random.randrange(62, 1439)
# 	ranY1 = random.randrange(161, 826)

# 	pyautogui.mouseDown()
# 	pyautogui.moveTo(ranX1, ranY1, 0)
# 	pyautogui.mouseUp()

def drawLine(x, y, x1, y1):
	pyautogui.mouseDown(x, y)
	pyautogui.moveTo(x1, y1, 0)
	pyautogui.mouseUp(x1, y1)



import pyautogui
import os
import random

os.system("sleep 2")

# ranX = random.randrange(62, 1439)
# ranY = random.randrange(161, 826)

# pyautogui.mouseDown(ranX, ranY)

for i in range(1, 50):
	ranX1 = random.randrange(62, 1439)
	ranY1 = random.randrange(161, 826)

	pyautogui.mouseDown()
	pyautogui.moveTo(ranX1, ranY1, 0)
	pyautogui.mouseUp()

def drawLine(x, y, x1, y1):
	pyautogui.mouseDown(x, y)
	pyautogui.moveTo(x1, y1, 0.25)
	pyautogui.mouseUp(x1, y1)

# drawLine(550, 620, 860, 620)
# drawLine(860, 620, 860, 340)
# drawLine(860, 340, 550, 340)
# drawLine(550, 340, 550, 620)

# drawLine(550 + 100, 620 + 100, 860 + 100, 620 + 100)
# drawLine(860 + 100, 620 + 100, 860 + 100, 340 + 100)
# drawLine(860 + 100, 340 + 100, 550 + 100, 340 + 100)
# drawLine(550 + 100, 340 + 100, 550 + 100, 620 + 100)

# drawLine(550 + 100, 620 + 100, 550, 620)
# drawLine(860 + 100, 620 + 100, 860, 620)
# drawLine(860 + 100, 340 + 100, 860, 340)
# drawLine(550 + 100, 340 + 100, 550, 340)

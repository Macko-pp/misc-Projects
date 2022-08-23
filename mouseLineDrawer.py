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


drawLine(429, 203, 589, 363)
drawLine(589, 363, 428, 364)
drawLine(428, 364, 429, 203)

drawLine(643, 201, 783, 281)
drawLine(783, 281, 644, 363)
drawLine(644, 363, 643, 201)

drawLine(860, 178, 981, 383)
drawLine(981, 383, 860, 300)
drawLine(860, 300, 860, 178)

drawLine(527, 387, 592, 477)
drawLine(592, 477, 527, 568)
drawLine(527, 568, 420, 534)
drawLine(420, 534, 420, 422)
drawLine(420, 422, 527, 387)

drawLine(699, 379, 781, 427)
drawLine(781, 427, 782, 519)
drawLine(782, 519, 700, 569)
drawLine(700, 569, 617, 521)
drawLine(617, 521, 617, 428)
drawLine(617, 428, 699, 379)

drawLine(862, 383, 937, 386)
drawLine(937, 386, 993, 438)
drawLine(993, 438, 994, 514)
drawLine(994, 514, 939, 569)
drawLine(939, 569, 861, 569)
drawLine(861, 569, 809, 514)
drawLine(809, 514, 809, 440)
drawLine(809, 440, 862, 383)

drawLine(468, 589, 529, 590)
drawLine(529, 590, 530, 650)
drawLine(530, 650, 591, 652)
drawLine(591, 652, 591, 713)
drawLine(591, 713, 530, 712)
drawLine(530, 712, 530, 775)
drawLine(530, 775, 468, 775)
drawLine(468, 775, 468, 715)
drawLine(468, 715, 406, 712)
drawLine(406, 712, 405, 651)
drawLine(405, 651, 465, 652)
drawLine(465, 652, 468, 589)

drawLine(606, 583, 797, 693)
drawLine(797, 693, 796, 757)
drawLine(796, 757, 603, 647)
drawLine(603, 647, 606, 583)

drawLine(814, 587, 985, 758)
drawLine(985, 758, 987, 587)
drawLine(987, 587, 812, 758)
drawLine(812, 758, 814, 587)

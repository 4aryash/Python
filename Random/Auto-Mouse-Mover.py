#pip install pyautogui

import pyautogui as pag
import random
import time

while True:
  x = random.randint(1200,1600)
  y = random.randint(400,800)
  pag.moveTo(x,y)
  time.sleep(1)

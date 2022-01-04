import pyautogui as pt
from time import sleep

while True:
    pos = pt.position()
    print(pos, pt.pixel(pos[0], pos[1]))
    sleep(1)

    if pos[0] == 0:
        break

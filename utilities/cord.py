import pyautogui
import time

time.sleep(1)

print(pyautogui.position())

pyautogui.confirm(pyautogui.position(), buttons=['готово'])
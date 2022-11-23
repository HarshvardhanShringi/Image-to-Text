from PIL import ImageGrab
import time
import pyautogui
import pyperclip
from PIL import Image
from pytesseract import pytesseract
import cv2



time.sleep(4)
# print(pyautogui.position())
pyperclip.copy('')
pyautogui.click(x=393, y=551, clicks=1, interval=0, button='right')
# #pyautogui.dragTo(602, 549, duration=0.5)
time.sleep(2)
pyautogui.click(x=468, y=635, clicks=1, interval=0, button='left')
#pyautogui.hotkey('ctrl', 'c')
# time.sleep(2)
# pyautogui.hotkey('ctrl','c')
time.sleep(1)
img = ImageGrab.grabclipboard()
#img.save(Desktop/new_img.jpg)

print(img)
print(img.mode)
img.show()
time.sleep(2)
pyautogui.screenshot('foo.png')
time.sleep(1)
pyautogui.click(x=1894, y=21, clicks=1, interval=0, button='left')
pyautogui.moveTo(x=600,y=500,duration=1)

import cv2

image = cv2.imread('foo.png')
y=300
x=400
h=1100
w=1100
crop = image[y:y+h, x:x+w]

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
print(pytesseract.image_to_string(crop))


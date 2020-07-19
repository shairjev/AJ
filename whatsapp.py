import webbrowser
import time
import pyautogui as gui

interval = 2
position = 814,405
numbers={911231231234}
message="hello"
for i in numbers:
 url = 'https://wa.me/{}?text={}'.format(i, message)
 webbrowser.open(url)
 time.sleep(3)
 gui.click(position)
 time.sleep(2)
 gui.press('enter')
 time.sleep(interval)


import webbrowser
import time
import pyautogui as gui

cameraposition=460,604
micposition=390,606
joinnowposition=903,459
settingsposition=1252,683
recordposition=1129,285
recordacceptposition=863,512

url='https://meet.google.com/atd-agpn-xyf'
webbrowser.open(url)

time.sleep(8)
gui.click(cameraposition)
time.sleep(2)
gui.click(micposition)
time.sleep(2)
gui.click(joinnowposition)
time.sleep(2)
gui.click(settingsposition)
time.sleep(2)
gui.click(recordposition)
time.sleep(2)
gui.click(recordacceptposition)
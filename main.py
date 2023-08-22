import pyautogui as py
import time

screenH, scrW = py.size()
#write the time on second after when you want to start your meeting
x=400 # after 400 sec you will join zoom automaticly for example!!
time.sleep(x)
#----------------------------------------------------------------------------
py.hotkey('win')
time.sleep(0.5)
py.typewrite('zoom')
time.sleep(1)
py.hotkey('enter')
time.sleep(2)
py.hotkey('win', 'up')
time.sleep(1.5)
py.moveTo(484,459)

py.click()
time.sleep(2)
id_meeting='73457094752'
py.typewrite(id_meeting)
time.sleep(1)
py.press('enter')
time.sleep(2)
py.hotkey('ctrl', 'Shift', 'm')
time.sleep(2)

py.hotkey('alt', 'a')



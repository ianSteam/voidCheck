import os
import keyboard
import time
import random
import string
import pyautogui  # type: ignore
import schedule # type: ignore
import time

import random
try:
    open("seedlist.txt", "x")
except:
    print("file probably already created. ignoring...")
else:
    print("seed list file created.")
try:
    open("seedlistFAIL.txt", "x")
except:
    print("file probably already created. ignoring...")
else:
    print("seed list file created.")

open("seedlist.txt", "a").write("\n")
runloop = 1
run = 1
md = 0
pd = 0
def restart2(x):
    keyboard.press_and_release("alt + f4")
#    print("reset moment")
    global seedb
    open("seedlistFAIL.txt", "a").write(f"{seedb}\n")
    global runloop
    runloop = 1
def restart(x):
    keyboard.press_and_release("alt + f4")
#    print("reset moment")
    global seedb
    open("seedlist.txt", "a").write(f"{seedb}\n")
    global runloop
    runloop = 1

schedule.every(30).minutes.do(restart2)
while run == 1:
    #t = Timer(30 * 60, restart)
    #t.start()
    #t.join()
    schedule.run_pending()
    if runloop == 1:
        seed = ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=random.randint(1, 10)))
        #seed = "insertseed"
        seedb = seed
        print(f"Using seed {seedb}...")
        os.popen(r'"c:/Users/unkl0kk/Desktop/SourceVoid Online/SourcevoidOnline.exe"')
        time.sleep(5)
        pyautogui.click(885, 646)
        keyboard.write(f"{seedb}")
        pyautogui.click(1492, 933)
        runloop = 0
    elif runloop != 1 and pyautogui.pixel(1029, 1388) != (0, 0, 0):
        restart(1)
while md == 1:
    print(pyautogui.position())
while pd == 1:
    #print(pyautogui.pixel(1179, 1388))
    if pyautogui.pixel(1029, 1388) != (0, 0, 0):
        print(pyautogui.pixel(1179, 1388))

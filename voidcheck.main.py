#library imports
import os
import keyboard
import time
import random
import string
import pyautogui  # type: ignore
import schedule # type: ignore
import time
import tkinter as tk
from pathlib import Path

# txt file setup and check
h = tk.Tk().winfo_screenheight()
w = tk.Tk().winfo_screenwidth()
import random
try:
    open("seedlist.txt", "x")
except:
    print("file probably already created. ignoring...")
try:
    open("seedlistFAIL.txt", "x")
except:
    print("file probably already created. ignoring...")
open("seedlist.txt", "a").write("\n")
runloop = 1
run = 1
md = 0
pd = 0

# determine executable path: read path.txt in the script directory or ask the user
script_dir = Path(__file__).parent
path_file = script_dir / "path.txt"
exe_path = None
if path_file.exists():
    try:
        exe_path = path_file.read_text(encoding="utf-8").strip()
        if exe_path == "":
            exe_path = None
    except Exception:
        exe_path = None

if not exe_path:
    # ask user for the full path to the executable and save it
    exe_path = input("Enter full path to SourcevoidOnline.exe: ").strip().strip('"')
    try:
        path_file.write_text(exe_path, encoding="utf-8")
        print(f"Saved executable path to {path_file}")
    except Exception as e:
        print(f"Warning: couldn't write path file: {e}")

if exe_path and not Path(exe_path).exists():
    print(f"Warning: the provided executable path does not exist: {exe_path}")

# reset function but for failed seeds
def restart2():
    keyboard.press_and_release("alt + f4")
#    print("reset moment")
    global seedb
    open("seedlistFAIL.txt", "a").write(f"{seedb}\n")
    global runloop
    runloop = 1

# reset function for working seeds
def restart():
    keyboard.press_and_release("alt + f4")
#    print("reset moment")
    global seedb
    open("seedlist.txt", "a").write(f"{seedb}\n")
    global runloop
    runloop = 1

# if it dosent find a seed in 30 minutes, restart and put seed in failed list
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
        # launch the configured executable (wrap in quotes in case path contains spaces)
        if exe_path:
            os.popen(f'"{exe_path}"')
        else:
            # fall back to the original hard-coded path if user left entry blank
            os.popen(r'"c:/Users/unkl0kk/Desktop/SourceVoid Online/SourcevoidOnline.exe"')
        time.sleep(5)
        pyautogui.click(w / 2.9, h / 2.25)
        keyboard.write(f"{seedb}")
        pyautogui.click(w / 1.71, h / 1.55)
        time.sleep(.5)
        keyboard.press_and_release("f")
        time.sleep(.5)
        keyboard.press_and_release("f")
        runloop = 0
    elif runloop != 1 and pyautogui.pixel(int(w/2), int(h-50)) != (0, 0, 0):
        restart()
while md == 1:
    print(pyautogui.position())
while pd == 1:
    #print(pyautogui.pixel(1179, 1388))
    if pyautogui.pixel(1029, 1388) != (0, 0, 0):
        print(pyautogui.pixel(1179, 1388))



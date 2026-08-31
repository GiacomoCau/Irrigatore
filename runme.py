
import os, time, subprocess
import psutil # pip install psutil

import config
mtime = os.path.getmtime(config.__file__)

print("Irrigatore started")
print("------------------------")
python = "python"
irrigatore = "C:\\Users\\Giacomo\\Documents\\Famiglia\\Davide\\Irrigatore\\irrigatore.py"
command = [python, irrigatore] 

process = subprocess.Popen(command , shell=True)
while True:
    time.sleep(30)
    mtime2 = os.path.getmtime(config.__file__)
    if mtime2 == mtime: continue
    for child in psutil.Process(process.pid).children(recursive=True): child.kill()
    process.kill()
    mtime = mtime2
    process = subprocess.Popen(command , shell=True)
    print("\nIrrigatore restarted")
    print("------------------------")

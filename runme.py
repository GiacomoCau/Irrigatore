
import os, time, subprocess

import config
mtime = os.path.getmtime(config.__file__)

command = ['python', 'irrigatore.py'] 
process = subprocess.Popen(command)
print('Irrigatore started')
while True:
    print('------------------------')
    time.sleep(30)
    mtime2 = os.path.getmtime(config.__file__)
    if mtime2 == mtime: continue
    process.kill()
    mtime = mtime2
    process = subprocess.Popen(command)
    print("\nIrrigatore restarted")

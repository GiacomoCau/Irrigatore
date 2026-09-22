import sys, config, os, psutil, time as tm
#import RPi.GPIO as gpio
from GPIOEmulator.EmulatorGUI import GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

delay = 1/30 # 0 nessun delay, 1 delay effettivo, 1/12 delay 5" per 1', 1/3600 delay 1" per 1h
def sleep(minuti):
    if delay > 0: tm.sleep(minuti*60*delay)

ps = sys.argv[1].split()
#print(ps)
#print(config.progs[ps[0]])
durate = sorted(config.progs[ps[0]][2]) if len(ps) == 1 else [[s,m] for (s,m) in config.progs[ps[0]][2] if s == int(ps[1])]
#print(durate)
stazioni = [4, 17, 18, 27, 22, 23, 24, 25]
for [s,m] in durate: 
    stazione = stazioni[s-1]
    gpio.setup(stazione, gpio.OUT)
    gpio.output(stazione, gpio.HIGH)
    sleep(m)
    gpio.output(stazione, gpio.LOW)
psutil.Process(os.getpid()).kill()
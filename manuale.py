
import sys, config, os, psutil
from util import stazioni, sleep, gpio 

ps = sys.argv[1].split()

if ps[0].isdigit():
    stazione = stazioni[int(ps[0])-1]
    gpio.output(stazione, gpio.HIGH)
else:
    durate = sorted(config.progs[ps[0]][2]) if len(ps) == 1 else [[s,m] for (s,m) in config.progs[ps[0]][2] if s == int(ps[1])]
    for [s,m] in durate: 
        stazione = stazioni[s-1]
        gpio.output(stazione, gpio.HIGH)
        sleep(m)
        gpio.output(stazione, gpio.LOW)
psutil.Process(os.getpid()).kill()
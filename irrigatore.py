
import datetime as dt
import time as tm

#from datetime import time as hm
#def sm(s, m): return [s, m]
import config, os
mtime = dt.date.fromtimestamp(os.path.getmtime(config.__file__))

#import RPi.GPIO as gpio
from GPIOEmulator.EmulatorGUI import GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

stazioni = [4, 17, 18, 27, 22, 23, 24, 25]
for s in stazioni: gpio.setup(s, gpio.OUT)
maxS = len(stazioni)


def invert (d):
    i = {}
    for k, vs in d.items():
        for v in vs: i.setdefault(v, []).append(k)
    return i

def isToday (now, tipo, *param):
    match tipo:
        case 'every':
            return (now - mtime).days % param[0] == 0
        case 'odd':
            return now.day % 2 == 1
        case 'even':
            return now.day % 2 == 0
        case 'o/e':
            return now.day % 2 == param[0]
        case 'dow':
            return param[now.weekday()] == 1
        case _:
            print("invalid parameter₁:", param)
    
def today (*now):
    now = dt.datetime.today() if len(now) == 0 else now[0]
    date = now.date()
    progs = [p for (p, args) in config.giorni.items() if isToday(date, *args)]
    time = now.time()
    starts = sorted([(t, sorted(ps)) for (t, ps) in invert(config.orari).items() if t >= time and any(x in ps for x in progs)])
    durate = {p : sorted([[s, m] for (s, m) in ds if s >= 1 and s <= maxS]) for (p, ds) in config.durate.items()}
    return [[t, [[p, durate[p]] for p in ps if p in progs and p in durate]] for (t, ps) in starts]

#today(dt.datetime.combine(dt.datetime.today(), dt.time(8,30)))
#today(dt.datetime(2026,8,6,8,30))

delay = 1 # 0 nessun delay, 1 delay, 1/12 delay 5" per 1', 1/3600 1h per 1s

def sleep(minuti):
    if delay > 0: tm.sleep(minuti*60*delay)

def openStation(stazione, minuti):
    stazione = stazioni[stazione - 1]
    gpio.output(stazione, gpio.HIGH)
    sleep(minuti)
    gpio.output(stazione, gpio.LOW)
   
def execTasks (tasks, *now):
    now = (dt.datetime.today() if len(now) == 0 else now[0]).replace(second=0, microsecond=0)
    while True:
        print("now:", now)
        for (ora, programmi) in tasks:
            datet = dt.datetime.combine(now.date(), ora)
            #print("*", datet, now)
            if datet > now:
                minuti = int((datet - now).seconds / 60)
                print("delay", str(minuti)+"'")
                sleep(minuti)
                now = dt.datetime.today() if delay == 1 else now + dt.timedelta(minutes=minuti)  
            print(ora, "start")
            for (programma, durate) in programmi:
                print('  programma:', programma)
                for (stazione, minuti) in durate:
                    print('    stazione:', stazione, str(minuti)+'\'')
                    openStation(stazione, minuti)
                    now = dt.datetime.today() if delay == 1 else now + dt.timedelta(minutes=minuti)
        minuti = int((dt.datetime.combine(now.date() + dt.timedelta(1), dt.time(0)) - now).seconds / 60)
        print('delay', str(minuti)+"'", 'fino alle', now+dt.timedelta(minutes=minuti), 'di domani\n')
        sleep(minuti)
        now = dt.datetime.today() if delay == 1 else now + dt.timedelta(minutes=minuti)
        tasks = today(now)

delay = 1/3600 # delay 1" per 60' ... 24" per 1gg
execTasks(today())

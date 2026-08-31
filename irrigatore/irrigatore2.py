
import datetime as dt
import time as tm

import importlib

#import RPi.GPIO as gpio
from GPIOEmulator.EmulatorGUI import GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

maxStaz = 8
stazioni = [4, 17, 18, 27, 22, 23, 24, 25]
for s in stazioni: gpio.setup(s, gpio.OUT)

def isToday (now, tipo, *param):
    match tipo:
        case 'every':
            return (now - param[1]).days % param[0] == 0
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
    data = importlib.import_module("data")
    now = dt.datetime.today() if len(now) == 0 else now[0]
    date = now.date()
    time = now.time()
    progs = [k for (k, v) in data.giorni.items() if isToday(date, *v)]
    starts = [(k, v) for (k, v) in data.orari.items() if k >= time]
    return [[k, [[p, data.durate[p]] for p in v if p in progs]] for (k, v) in starts]

delay = 1 # 0 nessun delay, 1 delay, 1/12 delay 5" per 1'

def sleep(minuti):
    if delay > 0: tm.sleep(minuti*60*delay)

def openStation(stazione, minuti):
    stazione -= 1
    gpio.output(stazioni[stazione], gpio.HIGH)
    sleep(minuti)
    gpio.output(stazioni[stazione], gpio.LOW)
   
def execTasks (tasks, *now):
    #print("tasks:", tasks)
    now = dt.datetime.today().replace(second=0, microsecond=0) if len(now) == 0 else now[0]
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
    #print(now)
    minuti = int((dt.datetime.combine(now.date() + dt.timedelta(1), dt.time(0)) - now).seconds / 60)
    print('delay', str(minuti)+"'", 'fino alle', now+dt.timedelta(minutes=minuti), 'di domani')
    #sleep(minuti)
    #now = dt.datetime.today() if delay == 1 else now + dt.timedelta(minutes=minuti)  
    #print('finito')

#import os
#os.path.getmtime(data.__file__)

def test (n):
    global delay
    match n:
        case 1:
            delay = 1/240
            tasks = today(dt.datetime.combine(dt.datetime.today(), dt.time(8,30)))
            #print(tasks)
            execTasks(tasks, dt.datetime.combine(dt.datetime.today(), dt.time(8,30)))
        case 2:
            delay = 1/12
            def addm(now, m): return (now + dt.timedelta(minutes=m)).time()
            now = dt.datetime.today().replace(second=0, microsecond=0)
            tasks = [[addm(now, 2), [['a', ((1, 1), (2, 1))], ['b', ((3, 1), (4, 1))]]], [addm(now, 8), [['c', ((1, 1),)]]], [addm(now, 11), [['a', ((1, 1), (2, 1))]]]]
            #print(tasks)
            execTasks(tasks, now)
    print()

#test(1)
while True:
    test(1)
    print("------------------------")
    sleep(4)

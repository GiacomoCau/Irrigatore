
import time as tm
import config

stazioni = [4, 17, 18, 27, 22, 23, 24, 25]

delay = 1/3600 # 0: nessun sleep, 1: sleep effettivo, 1/12: 5" per 1', 1/30: 2" per 1', 1/60 1" per 1', 1/3600: 1" per 1h
def sleep(minuti):
    minuti *= config.perc / 100
    if delay > 0: tm.sleep(minuti*60*delay)

#import RPi.GPIO as gpio
from GPIOEmulator.EmulatorGUI import GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

for s in stazioni: gpio.setup(s, gpio.OUT)

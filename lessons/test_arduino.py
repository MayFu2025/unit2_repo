#test arduino

import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-110')
print('Connected to Arduino')

data=pyfirmata.util.Iterator(board)
data.start()

LED_13 = board.digital[13]
LED_13.mode = pyfirmata.OUTPUT
LED_13.write(0)

t=100
while t>0:
    LED_13.write(1) #Turn on LED
    time.sleep(0.5)
    LED_13.write(0) #Turn off LED
    time.sleep(0.5)

exit()
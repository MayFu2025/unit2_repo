import pyfirmata
from pyfirmata import Arduino
import time

questions= {
    "Today is a Monday": "No",
    "1+1=2": "Yes",

}

board = Arduino('/dev/cu.usbserial-10')
print("Connection Successful")

it = pyfirmata.util.Iterator(board)
it.start()

yes = board.digital[9]
yes.mode = pyfirmata.INPUT

no = board.digital[4]
no.mode = pyfirmata.INPUT

LED = board.digital[2]
LED.mode = pyfirmata.OUTPUT
LED.write(0)

for question in questions.keys():
    print(question)
    answer = questions[question]
    while yes.read() == 0 and no.read() == 0:
        time.sleep(0.1)
    if yes.read == 1 and answer == "Yes":
            print("You are correct!")
            LED.write(1)
    elif no.read == 1 and answer == "No":
            print("You are correct!")
            LED.write(1)
    else:
        print("You are wrong!")
    time.sleep(1)
    yes.write(0)
    no.write(0)



while True:
    yes_state = yes.read()
    no_state = no.read()
    if yes_state == 1:
        LED.write(1)
    else:
        LED.write(0)




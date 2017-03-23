from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)
while True:
    print("OUT")
    O = [255, 127, 80]  
    X = [0, 0, 0]
    nit1 = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, O, O, X, X, X,
    X, X, X, O, O, X, X, X,
    X, X, X, X, X, X, X, X,
    O, O, O, X, O, X, O, O,
    O, X, O, X, O, X, O, X
    ]

    nit2 = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, O, O, X, X, X,
    X, X, X, O, O, X, X, X,
    X, X, X, X, X, X, X, X,
    O, X, O, X, O, O, O, X,
    O, X, O, X, X, O, X, X
    ]

    nit3 = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, O, O, X, X, X,
    X, X, X, O, O, X, X, X,
    X, X, X, X, X, X, X, X,
    X, O, X, O, 0, O, X, X,
    X, O, X, X, O, X, X, X
    ]
    sense.set_pixels(nit1)
    time.sleep(0.5)
    sense.set_pixels(nit2)
    time.sleep(0.5)
    sense.set_pixels(nit1)
    time.sleep(0.5)
    sense.show_message("Currently In Pradeeps Room", text_colour=O)
    time.sleep(0.5)

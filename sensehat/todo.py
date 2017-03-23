from sense_hat import SenseHat
import time

class ToDO:
    "A simple to do scroller for sense hat"
    sense= SenseHat()
    a = ['Merge Sort',
        'Inversion',
        'NP Complete',
        'WEB SERVER RUNNING... DO NOT POWER OFF']
    def __init__(self):
        print("initialized")
        #self.sense.set_rotation(180)
        self.sense.low_light=True

    def scroll(self):
        for i in range(0, len(self.a)):
            #print(i)
            self.sense.show_letter(str(i))
            time.sleep(1)
            self.sense.show_message(self.a[i])
            time.sleep(1)

    def scrollLeft(self):
        X=[0, 50, 0]
        O=[0, 0, 0]
        stop = [O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            X, X, X, X, O, O, O, O
            ]
        self.sense.set_pixels(stop)
        time.sleep(1);
        self.sense.clear();

        stop = [O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, X, X, X, X, O, O, O
            ]
        self.sense.set_pixels(stop)
        time.sleep(1);
        self.sense.clear();

        stop = [O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, X, X, X, X, O, O
            ]
        self.sense.set_pixels(stop)
        time.sleep(1);
        self.sense.clear();

t = ToDO()
#t.sense.load_image("space_invader.png")
#time.sleep(10)
while True:
    t.scrollLeft() 

from sense_hat import SenseHat
import time

def mail() :
    X=[0, 0, 0]
    O=[0, 50, 0]
    stop = [O, O, O, O, O, O, O, O,
            O, O, X, X, X, X, O, O,
            O, X, O, X, X, O, X, O,
            O, X, X, O, O, X, X, O,
            O, X, X, X, X, X, X, O,
            O, X, X, X, X, X, X, O,
            O, X, X, X, X, X, X, O,
            O, O, O, O, O, O, O, O
            ]
    sense.set_pixels(stop)
    time.sleep(1)
    sense.clear()
    time.sleep(1)
    sense.set_pixels(stop)
    time.sleep(1)
    sense.clear()
    time.sleep(1)
    sense.set_pixels(stop)
    time.sleep(1)
    sense.clear()
    
def pushed_up(event):
    print("Button up")
    global lbreak
    lbreak = True
    global col_index
    col_index = (col_index +1) %3

def pushed_down(event):
    print("Button Down")
    global lbreak
    lbreak = True
    global col_index
    col_index = (col_index -1)
    if col_index < 0:
        col_index = 2

def pushed_left(event):
    print("Pushed left")
    global lbreak
    lbreak = True
    sense.clear()
    if event.action=="pressed":
        global cur_function
        cur_function = (cur_function+1)%6
    sense.show_letter(str(cur_function))
    time.sleep(1)

def pushed_right(event):
    print("Pushed Right")
    global lbreak
    lbreak = True
    if event.action=="pressed":
        global cur_function
        cur_function = (cur_function -1)
        if cur_function < 0:
            cur_function = 5
    sense.show_message(str(cur_function))
    time.sleep(1)
    
def init():
    print("Init")
    global lbreak;
    #mail()
    showwelcome()
    if lbreak == True:
        lbreak = False
        return
    temp()
    if lbreak == True:
        lbreak = False
        return
    humidity()
    if lbreak == True:
        lbreak = False
        return
    #sense.show_message("USE JOYSTICK TO SET PARTICULAR",text_colour=[51,0 ,102 ], back_colour=[229,255, 204])

def busy_f():
    print("Busy")
    O = [50, 0, 0]  
    X = [0, 0, 0]
    question_mark = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
        ]
    sense.set_pixels(question_mark)
    time.sleep(1)
    sense.show_message("BUSY", text_colour=O);
    time.sleep(speed+speed)

def available_f():
    print("available")
    O = [0, 50, 0]  
    X = [0, 0, 0] 
    question_mark = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
        ]
    sense.set_pixels(question_mark)
    time.sleep(1)
    sense.show_message("FREE", text_colour=O);
    time.sleep(speed+speed)

def show_drop(text_c):
    sense.clear()
    time.sleep(0.5)
    O = [0, 50, 0]  
    X = [0, 0, 0] 
    drop = [
        O, O, O, O, O, O, O, O,
        X, O, O, O, O, O, O, X,
        X, X, O, O, O, O, X, X,
        X, X, X, O, O, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
        ]
    sense.set_pixels(drop)
    time.sleep(0.5)

def show_raise(text_c):
    sense.clear();
    time.sleep(0.5)
    O = [50, 0, 0]  
    X = [0, 0, 0] 
    inc = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, O, O, X, X, X,
        X, X, O, O, O, O, X, X,
        X, O, O, O, O, O, O, X,
        O, O, O, O, O, O, O, O
        ]
    sense.set_pixels(inc)
    time.sleep(0.5)

def showwelcome():
    print("Welcome")
    global global_colour
    global col_index
    global lbreak
    time.sleep(1);
    sense.set_rotation(90)
    sense.show_message(":)", text_colour = [0,50,0])
    sense.set_rotation(0)
    #sense.show_message("SERVER IS UP.. DO NOT UNPLUG OR DISCONNECT", text_colour=[60,0,0])

    time.sleep(1)
    sense.show_letter("N", text_colour = global_colour[col_index])
    time.sleep(0.5)    
    sense.show_letter("I", text_colour = global_colour[col_index])
    time.sleep(0.5)
    sense.show_letter("T", text_colour = global_colour[col_index])
    if lbreak == True:
        return
    time.sleep(0.5)
    sense.show_letter("H", text_colour = global_colour[col_index])
    time.sleep(0.5)
    sense.show_letter("I", text_colour = global_colour[col_index])
    time.sleep(0.5)
    sense.show_letter("N", text_colour = global_colour[col_index])
    time.sleep(0.5)
    sense.show_letter(" ", text_colour = global_colour[col_index])
    time.sleep(0.5)
    #sense.show_message("DEVANG", text_colour = global_colour[col_index])
    time.sleep(0.5)
    return

def temp():
    print("temperature")
    global global_colour
    global col_index
    global lbreak
    global speed
    global global_high
    global global_low
    
    temp = sense.get_temperature()
    temp = round(((temp-32) * (5/9)), 1)
    #print(temp)
    global cur

    while temp >5 or temp < -2 :
        temp = sense.get_temperature()
        temp = round(((temp-32) * (5/9)), 1)
        X= [50, 0, 0]
        if temp <-2:
            X=[0, 50, 0]
        stop = [X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X,
                X, X, X, X, X, X, X, X
                ]
        sense.set_pixels(stop)
        time.sleep(1)
        sense.clear()
        time.sleep(1)

        sense.set_pixels(stop)
        time.sleep(1)
        sense.clear()
        time.sleep(1)

        sense.set_pixels(stop)
        time.sleep(1)
        sense.clear()
        time.sleep(1)
        sense.show_message(str(temp), text_colour=[50,0,0])
        humidity()
    sense.clear()
    text_c = [0, 0, 150]
    change = 0 #no change
    
    if temp > cur+0.3:
        change = 1 #positive
        text_c = [50, 0, 0]
        cur = temp
        
    elif temp < cur-0.3:
        text_c = [0, 50, 0]
        change = -1 #negative
        cur = temp
    sense.show_message("Temperature = ", text_colour=text_c)
    #sense.show_letter("T", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("E", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("M", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("P", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("E", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("R", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("A", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("T", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("U", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("R", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)
    #sense.show_letter("E", text_colour=text_c)
    #sense.set_pixel(0, 0, text_c)
    #time.sleep(speed)

    if change >0:
        show_raise(text_c)
        show_raise(text_c)
        show_raise(text_c)
        show_raise(text_c)
    elif change <0:
        show_drop(text_c)
        show_drop(text_c)
        show_drop(text_c)
        show_drop(text_c)
    else:
        sense.show_letter("=", text_colour = text_c)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)
        
        #sense.show_letter("=", text_colour = text_c)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)
        
        #sense.show_letter("=", text_colour = text_c)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)

        sense.show_letter("=", text_colour = text_c)
        time.sleep(0.5)
    
    sense.show_message(str(temp), text_colour=text_c)
    if cur > global_high:
        global_high = cur
        #sense.show_message("REACHED ALL TIME HIGH TEMP", text_colour = [255, 0, 0])
    if cur < global_low:
        global_low = cur
        #sense.show_message("REACHED ALL TIME LOW TEMP", text_colour = [0, 255, 0])
    return

def humidity():
    print("Humidity")
    global global_colour
    global col_index
    sense.show_message("HUMIDITY = ", text_colour = global_colour[col_index+2])
    sense.clear();
    humidity = round(sense.get_humidity(), 2)
    sense.show_message(str(humidity), text_colour = global_colour[col_index+1])
    time.sleep(3);
    return

sense = SenseHat()
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

#sense.set_rotation(180)
cur = sense.get_temperature()

global_colour = [[50,40 ,60 ], [50, 0, 40], [0, 50, 40]]
col_index = 0;
lbreak = False
speed = 0.2

global_high = cur
global_low = cur

cur_function =0


while True:
    #if cur_function < 0:
        #cur_function = 5
    if lbreak == True:
        lbreak = False
    #print(cur_function)
    if cur_function == 0:
        init()
    elif cur_function == 1:
        showwelcome()
    elif cur_function == 2:
        if lbreak == True:
            lbreak = False
            continue;
        time.sleep(3)
        temp()
    elif cur_function == 3:
        if lbreak == True:
            lbreak = False
            continue
        time.sleep(3)
        humidity()
    elif cur_function == 4:
        busy_f()
    elif cur_function == 5:
        available_f()

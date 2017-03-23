#!/usr/bin/env python3

# Importing needed modules of PyMySQL
from pymysql import connect, err, sys, cursors
from sense_hat import SenseHat
from gpiozero import MotionSensor
import time


def init():
    print("Init")
    showwelcome()
    temp()
    humidity()

def showwelcome():
    pir.wait_for_motion()
    print("Welcome")
    global global_colour
    global col_index
    time.sleep(1);
    sense.set_rotation(90)
    sense.show_message(":)", text_colour=[0, 50, 0])
    sense.set_rotation(0)

    time.sleep(1)
    sense.show_letter("N", text_colour=global_colour[col_index])
    time.sleep(0.3)
    sense.show_letter("I", text_colour=global_colour[col_index])
    time.sleep(0.3)
    sense.show_letter("T", text_colour=global_colour[col_index])
    time.sleep(0.3)
    sense.show_letter("H", text_colour=global_colour[col_index])
    time.sleep(0.3)
    sense.show_letter("I", text_colour=global_colour[col_index])
    time.sleep(0.3)
    sense.show_letter("N", text_colour=global_colour[col_index])
    time.sleep(0.3)
    sense.show_letter(" ", text_colour=global_colour[col_index])
    time.sleep(0.3)
    time.sleep(0.3)
    return


def temp():
    pir.wait_for_motion()
#    print("temperature")
    global global_colour
    global col_index
    global speed
    global global_high
    global global_low

    temp = sense.get_temperature()
    #temp = round(((temp - 32) * (5 / 9)), 1)
    temp = round(temp, 1);
    #print(temp)
    global cur
    global hUpdate;

    while temp > 29 or temp < 6:
        temp = sense.get_temperature()
        temp = round(temp, 1)
        X = [50, 0, 0]
        if temp < 6:
            X = [0, 50, 0]
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
        updateDbTemp(str(temp));
        sense.show_message(str(temp), text_colour=[50, 0, 0])
        humidity()
    sense.clear()
    text_c = [0, 0, 150]
    change = 0  # no change

    if temp > cur + 0.3:
        change = 1  # positive
        text_c = [50, 0, 0]
        cur = temp

    elif temp < cur - 0.3:
        text_c = [0, 50, 0]
        change = -1  # negative
        cur = temp
    sense.show_message("Temperature = ", text_colour=text_c)
    if change > 0:
        show_raise(text_c)
        show_raise(text_c)
        show_raise(text_c)
        show_raise(text_c)
    elif change < 0:
        show_drop(text_c)
        show_drop(text_c)
        show_drop(text_c)
        show_drop(text_c)
    else:
        sense.show_letter("=", text_colour=text_c)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)

        # sense.show_letter("=", text_colour = text_c)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)

        # sense.show_letter("=", text_colour = text_c)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)

        sense.show_letter("=", text_colour=text_c)
        time.sleep(0.5)

    updateDbTemp(str(temp));
    sense.show_message(str(temp), text_colour=text_c)
    if cur > global_high:
        global_high = cur
        # sense.show_message("REACHED ALL TIME HIGH TEMP", text_colour = [255, 0, 0])
    if cur < global_low:
        global_low = cur
        # sense.show_message("REACHED ALL TIME LOW TEMP", text_colour = [0, 255, 0])
    return


def humidity():
    pir.wait_for_motion()
    print("Humidity")
    global global_colour
    global col_index
    global hUpdate;
    sense.show_message("HUMIDITY = ", text_colour=global_colour[col_index + 2])
    sense.clear();
    humidity = round(sense.get_humidity(), 2)
    hUpdate = humidity;
    sense.show_message(str(humidity), text_colour=global_colour[col_index + 1])
    time.sleep(3);
    return

def updateDbTemp(temp):
    hum = str(round(sense.get_humidity(), 2));
    global cursor;
    cursor.execute("INSERT INTO temp_data(temp, hum) VALUES ("+temp+", "+hum+")")
    conn.commit()

def show_drop(text_c):
    pir.wait_for_motion()
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
    pir.wait_for_motion()
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





sense = SenseHat()
pir = MotionSensor(4)

# sense.set_rotation(180)
# Doing our connection
conn = connect(host='localhost',
               port=3306,
               user='user',
               passwd='passwword',
               db='niu_res');
cursor = conn.cursor(cursors.DictCursor);
cur = sense.get_temperature()
hUpdate = 0;

global_colour = [[50, 40, 60], [50, 0, 40], [0, 50, 40]]
col_index = 0;
lbreak = False
speed = 0.2

global_high = cur
global_low = cur

cur_function = 0

while True:
    init()


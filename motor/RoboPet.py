# Nithin Devang
#
from AMSpi import AMSpi
import time
from gpiozero import MotionSensor
from sense_hat import SenseHat


class RoboPet:
    "This is a robo pet example.__doc__."

    def moveLeft(self, amspi):  # Move left
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
        time.sleep(0.5)
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

    def moveRight(self, amspi):  # Move left
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
        time.sleep(0.5)
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

    def showSmile(self, sense):
        sense.clear();
        O = [255, 0, 0]
        X = [0, 0, 0]
        inc = [
            X, X, X, X, X, X, X, X,
            X, O, O, X, O, O, X, X,
            X, O, O, X, O, O, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, O, X,
            X, O, X, X, X, O, X, X,
            X, X, O, O, O, X, X, X,
            X, X, X, X, X, X, X, X
        ]
        sense.set_pixels(inc)

    def showSleep(self, sense):
        sense.clear();
        O = [0, 0, 255]
        X = [0, 0, 0]
        inc = [
            X, X, X, X, X, X, X, X,
            X, O, O, X, O, O, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, O, O, O, X, X, X,
            X, X, X, X, X, X, X, X
        ]
        sense.set_pixels(inc)




if __name__ == '__main__':
    # Calling AMSpi() we will use default pin numbering: BCM (use GPIO numbers)
    # if you want to use BOARD numbering do this: "with AMSpi(True) as amspi:"
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)

        RP = RoboPet()
        pir = MotionSensor(4)
        sense = SenseHat()

        while True:
            pir.wait_for_no_motion()
            print("Waiting for motion")
            pir.wait_for_motion()
            print("Motion detected")
            for i in range(0, 10):
                RP.showSmile(sense)
                RP.moveLeft(amspi)
                RP.moveRight(amspi)
            pir.wait_for_no_motion()
            sense.clear();
            RP.showSleep(sense)
            print("motion stopped")


        #print("Stop and Exit")
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

Sense1.py
> This project use sensehat and PIR motion sensor.
> This reads temperature and humidity from sensehat senors and displays it on the 8*8 LED matrix.
> It also pushes this value to DB.
> When no motion is detected it pauses the display.

TO DO:
> update db username and password in sense1.py at line 215 connect function.
	conn = connect(host='localhost',
               port=3306,
               user='user',
               passwd='passwword',
               db='niu_res');
> Motion sensor is conencted to GPIO 4. You may need to update this number if you are using other pin.
				pir = MotionSensor(4)
				
				
Web.
> Displays historical charts and current room temperature and humidity.
TO DO:
> Update db details in DataAccessLayer/DA_DataBaseConnectionClass.php

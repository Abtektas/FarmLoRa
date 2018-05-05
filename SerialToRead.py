import serial
from time import sleep
import datetime

FO = open("SensorValues.txt", "w")
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()

while True:    	    
	sleep(3)

	data = ser.readline(5)

	time = datetime.datetime.now().strftime("%H : %M : %S")

	print(data + 'Data came at : ' + time)

	FO.write(data + '\n')
	FO.flush()

FO.close()
ser.close()

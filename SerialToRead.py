import serial
from time import sleep
import datetime

FO = open("SensorValues.txt", "w")
Ser = serial.Serial()
Ser.baudrate = 9600
Ser.port = '/dev/ttyUSB0'
Ser.open()

while True:    	   
	
	sleep(60)

	Data = Ser.readline(5)

	Time = datetime.datetime.now().strftime("%H : %M")

	print(Data + 'Data came at : ' + Time)

	FO.write(Data + '\n')
	FO.flush()

FO.close()
Ser.close()

import pigpio
import serial
from time import sleep

pi = pigpio.pi()

import DHT22 

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()

s = DHT22.sensor(pi, 4)
s.trigger()
sleep(.03)

x = '{:3.2f}'.format(s.humidity() / 1.)
y = '{:3.2f}'.format(s.temperature() / 1.)

print (x) # For seeing values.
print (y) # For seeing values.

ser.write(x.encode()) #encoding to bytes. 
ser.write(y.encode()) #encoding to bytes.

s.cancel()
pi.stop()
ser.close()

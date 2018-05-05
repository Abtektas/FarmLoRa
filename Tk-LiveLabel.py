import Tkinter as tk
import serial
from time import sleep
import datetime

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()
 
def stats(label):
  
	def count():
    
		data = ser.readline(5)
		dataArray = data.split('\n')

		xar = []
		yar = []

		for eachLine in dataArray:

			if len(eachLine)>1:
				x,y = eachLine.split(',')

				xar.append(int(x))
				yar.append(int(y))

				xstr = str(xar)
				ystr = str(yar)

				xrw = 'Temperature : '+ xstr           
				yrw = 'Humidity : ' + ystr

		time = datetime.datetime.now().strftime("%H : %M : %S")		
		label2.config(text = 'Data came at ' + time)
		label.config(text = xrw + '\n' + yrw)
		label.after(1000, count)
		
	count()
 
root = tk.Tk()
root.title("Current stats : ")

label = tk.Label(root, fg="dark green", font=("Helvetica", 30))
label2 = tk.Label(root, fg='red', font=("Helvetica", 20))

label2.pack()
label.pack()
stats(label)

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

root.mainloop()

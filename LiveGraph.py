import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from time import sleep
import datetime

fig = plt.figure()
FirstPlot = fig.add_subplot(2,1,1)
SecondPlot = fig.add_subplot(2,1,2)

def animate(i):
	
	GetData = open("SensorValues.txt","r").read()
	DataArray = GetData.split('\n')

	x1 = []
	y1 = []

	for EachLine in DataArray:

		if len(EachLine)>1:
			x,y = EachLine.split(',')

			x1.append(int(x))
			y1.append(int(y))

			FirstPlot.clear()
			SecondPlot.clear()

			FirstPlot.plot(x1)
			SecondPlot.plot(y1)			

	Time = datetime.datetime.now().strftime("%H : %M")
	
	FirstPlot.set_title('Data came at' + ' ' + Time)
	FirstPlot.set_xlabel('Packet(line)')
	FirstPlot.set_ylabel('Celsius')

	SecondPlot.set_xlabel('Packet(line)')
	SecondPlot.set_ylabel('Percent')

	fig.tight_layout()
		
ani = animation.FuncAnimation(fig, animate, interval=60000)
plt.show()


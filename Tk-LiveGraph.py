import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from time import sleep

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

def animate(i):
	
	pullData = open("SensorValues.txt","r").read()
	dataArray = pullData.split('\n')

	xar = []
	yar = []

	for eachLine in dataArray:

		if len(eachLine)>1:
			x,y = eachLine.split(',')

			xar.append(int(x))
			yar.append(int(y))

			ax1.clear()
			ax2.clear()

			ax1.plot(xar)
			ax2.plot(yar)

	ax1.set_title('Temperature values per packets.')
	ax1.set_xlabel('Packet(line')
	ax1.set_ylabel('Celsius')

	ax2.set_title('Humidity values per packets')
	ax2.set_xlabel('Packet(line)')
	ax2.set_ylabel('Celsius')
	
	fig.tight_layout()
        
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


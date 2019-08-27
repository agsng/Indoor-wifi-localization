import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import multithread_position

style.use('fivethirtyeight')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def looper(i):
	count = 0
	x = []
	y = []
	x1 = 0
	y1 = 0
	count=count+1
	multithread_position.main()
	rasta=open("cood.csv")
	for points in rasta:
		x1,y1=points.split("\t")
		x.append(int(x1))
		y.append(int(y1))
	rasta.close()
	ax1.clear()
	ax1.axis([-8,8,-10,8])
	ax1.plot(x, y,'-bo')
	plt.annotate('You are here!', xy=(int(x1),int(y1)), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05),)
	#plt.clear()
	#b=input("input=")
	#if b=="a":
	#	print("broke>>>>>>>>>>>>>>>>>>>>a")
	#	break
	print("all done-->",count)

#-------------------------------------------------------------------------

ani = animation.FuncAnimation(fig,looper,interval=1000)
plt.show()



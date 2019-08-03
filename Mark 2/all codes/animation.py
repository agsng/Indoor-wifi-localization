import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    xs=[]
    ys=[]
    data=open("cood.csv")
    for lines in data:
        if len(lines)>1:
            x,y=lines.split("\t")
            xs.append(int(x))
            ys.append(int(y))
    data.close()
    ax1.clear()
    ax1.axis([-8, 8, -10, 8])
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
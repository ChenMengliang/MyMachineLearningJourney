import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
fig, ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def animat(i):
    line.set_ydata(np.sin(x+i/10.0))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,
                              func = animat,
                              frames=100,
                              init_func=init,
                              interval=200,
                              blit=False)
plt.show()

# x = np.linspace(-1, 1, 500)
# y1 = 2 * x + 1
# y2 = x ** 2
# plt.figure()
# plt.plot(x, y1)
# plt.plot(x, y2, color='red')
# plt.show()

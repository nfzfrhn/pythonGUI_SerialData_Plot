from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create empty list for the x and y data
x = []
y = []

# Create the figure and axes object
fig, ax = plt.subplots()

def animate(i):
    pt = randint(1,9)   # Grab a random integer to be the next y-value in the animation
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x,y)
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])

# Run the animation
ani = FuncAnimation(fig, animate, frames=50, interval=50, repeat=False)   

plt.show()

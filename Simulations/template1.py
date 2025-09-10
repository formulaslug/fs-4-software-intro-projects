import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    pass

def step (state:State) -> State:
    return state

def animate (i):
    pass

fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
plt.pause(5)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()
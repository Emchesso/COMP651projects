# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:55:53 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    theta = np.linspace(0, 4, 1000)
    start = i*4
    end = start + 4
    x = np.sin(2 * np.pi * theta[start:end])
    y = np.cos(2 * np.pi * theta[start:end])
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
               frames=200, interval=20, blit=True)
writergif = animation.PillowWriter(fps=30) 
anim.save('Assignment_7-5_gif', writer=writergif)

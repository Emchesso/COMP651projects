# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:18:12 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import matplotlib.pyplot as plt
import numpy as np

# Problem 1
def ReL(x):
    return max(0,x)

x = np.linspace(0.0,2.0,50)
x1 = np.sin(2*np.pi*x)
x2 = 0.4 * np.sin(8*np.pi*x)
x3 = x1 + x2
x4 = x1 + [ReL(x) for x in x2]

fig = plt.subplots(2,2,
                  sharex=True,
                  sharey=True)

plt.subplot(221)
plt.plot(x,x1,'b')
plt.gca().set_xticks([0,.5,1,1.5,2])
plt.gca().set_yticks([-1,0,1])
plt.grid(True)
plt.axhline(0, linewidth=1, color='k')
plt.title(r'$\mathrm{sin}(2\pi x)$')

plt.subplot(222)
plt.plot(x,x2,'c')
plt.gca().set_xticks([0,.5,1,1.5,2])
plt.gca().set_yticks([-1,0,1])
plt.grid(True)
plt.axhline(0, linewidth=1, color='k')
plt.title(r'$0.4\mathrm{sin}(8\pi x)$')

plt.subplot(223)
plt.plot(x,x3,'r')
plt.gca().set_xticks([0,.5,1,1.5,2])
plt.gca().set_yticks([-1,0,1])
plt.grid(True)
plt.axhline(0, linewidth=1, color='k')
plt.title(r'$\mathrm{sin}(2\pi x) + 0.4\mathrm{sin}(8\pi x)$')
plt.tight_layout()

plt.subplot(224)
plt.plot(x, x4, 'r')
plt.gca().set_xticks([0,.5,1,1.5,2])
plt.gca().set_yticks([-1,0,1])
plt.grid(True)
plt.axhline(0, linewidth=1, color='k')
plt.title(r'$\mathrm{sin}(2\pi x) + ReL(0.4\mathrm{sin}(8\pi x))$')

plt.savefig('Assignment_7-1_sin_graphs.png')

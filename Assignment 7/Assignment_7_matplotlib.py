# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:46:22 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# show() display in window
# draw() clears and draws new
# ion() ioff() interactive mode, displays images as they are created
# savefig('fig1.png') saves it in the code folder or jupyter notebook
# savefig('C:\\Users\\Ethan\\Documents\\School\\Spring 22\\COMP 651\\Assignments\\Assignment 7\\fig1.png')
# for saving in a specific directory
# emf, eps, pdf, png, ps, raw, rgba, svg, svgz supported, png default

# plot() 
# plt.plot([1,2,3,4]) with 1 dimensional array, assumes these are y-values, sets
# ass same length, starting at 0

# after x and y coordinates, color can be chosen (b,g,r,k,c, or RGB triplets)
# can add type of line here (-, --, -., :, o, +, x, D)
# axis() specifies view port with a list [xmin, xmax, ymin, ymax] or 
# plt.axis(xmin=0, xmax=6,
          # ymin=0, ymax=20)
# xlim() and ylim() return edge of graph area, can set with internal arguments
# plt.axis('off') suppresses axis
# bbox_inches='tight' removes extra perimeter area when savefig()
#

# plt.axis(([0,6,0,20]))
# plt.plot([0,4,3,5],[8,4,2,4], 'g-.')
# print(plt.xlim())
# print(plt.ylim())

# for multiple lines  arrange them thusly

# t = np.arange(0.0, 5.2, 0.2)
# plt.plot(t, t, t, t**2, 'rs', t, t**3, 'g^')

### other properties found in slides 19-21

# text commands xlabel(), ylabel(), title(), text(), take string arguments
# text() takes 3 args, x and y, and a string
# optional kwargs or dicts specify font properties, slides 23 for more
# setp() to set a property of text

# plt.plot([1,2,3])
# t = plt.xlabel('Time')

# plt.ylabel('Volts')
# plt.title('A Line')
# plt.text(0.5, 2.5, 'Peakaboo!')

# # plt.setp(t, color= 'r', fontweight='bold')
# labels = plt.getp(gca(), 'xticklabels')
# plt.setp(labels, color='r', fontweight='bold')

# mathematical expressions, use TeX
# plt.title(r'$\alpha > \beta$')
# subscript and superscript '_' and '^'
# other symbols (\infty, \leftarrow, \sum, \int) more on slides 28-31

# Problem 1
# x = np.linspace(0.0, 2.0, 50)
# plt.plot()

# t = np.arange(0.0, 2.0, 0.01)
# s = np.sin(2*np.pi*t)
# plt.plot(t,s)
# plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
# plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
# plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$', fontsize=20)
# plt.xlabel('time (s)')
# plt.ylabel('volts (mV)')
# plt.savefig('mathtext_tut', dpi=50)

# Multiple Figures slides 4459
# Figure contains all plot elements, Axes is the specific graph in a Figure
# Axis, Tick, Line2D, Text, Polygon are all elements of it
# gca() returns current axes as an Axes instance
# gcf() returns current figure as a Figure instance
# figure() returns an instance of figure

# plt.figure(1) 
# plt.plot([1,2,3])
# plt.figure(2) 
# plt.plot([4,5,6])
# plt.figure(1)    # make figure 1 current
# plt.title('Easy as 1,2,3')  

# These get displayed on top of each other in separate windows

# plt.plot([0.2, 0.4, 0.6, 0.8, 3]) # plot a regular graph
# ax1 = plt.gca()
# ax2 = plt.axes([0.25,0.45,0.25,0.25], fc='y')   # second graph, yellow background
# plt.axes(ax1) # set to ax1 for modification
# plt.plot([0.1,0.2,0.3,0.4,2], 'r--') # red dotted line
# plt.axes(ax2) # set to ax2 for mod
# plt.plot([1,2,3])
# plt.savefig('axes') # save to directory

# subplot(numRows, numCols, plotNum) to get other graphs
# plt.subplot(221)    #2 rows, 2 columns, 1st position
# plt.plot([1,2,3])   #set y coordinates
# plt.subplot(222)    #"                 "2nd position
# plt.plot([2,3,4])
# plt.subplot(223)
# plt.plot([1,2,3], 'r--')
# plt.subplot(224)
# plt.plot([2,3,4], 'r--')
# plt.subplot(221)
# plt.plot([3,2,1], 'r--')
# plt.savefig('subplot')


# more compact command is plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True)
# below shows this, with shared x and y axes

# import matplotlib.pyplot as plt
# fig, axs = plt.subplots(2, 2, 
#                   sharex=True,
#                   sharey=True)
# axs[0,0].plot([1,2,3])
# axs[0,0].set_title("Subplot 1")
# axs[0,1].plot([2,3,4])
# axs[0,1].set_title("Subplot 2")
# axs[1,0].plot([1,2,3], 'r--')
# axs[1,0].set_title("Subplot 3")
# axs[1,1].plot([2,3,4], 'r--')
# axs[1,1].set_title("Subplot 4")
# axs[0,0].plot([3,2,1], 'r--')
# plt.savefig('subplots')

# Ticks
# plt.plot([1,2,3])
# # [<matplotlib.lines.Line2D object at 0x01C9C110>]
# plt.gca().set_xticks([0.25, 0.75, 1.25, 1.75, 2.25, 2.75], minor=True)
# # [<matplotlib.axis.XTick object at 0x00B3B770>,
# #  <matplotlib.axis.XTick object at 0x02AC9C10>,
# #  <matplotlib.axis.XTick object at 0x02AC9F90>,
# #  <matplotlib.axis.XTick object at 0x02AC9FF0>,
# #  <matplotlib.axis.XTick object at 0x02AD4390>,
# #  <matplotlib.axis.XTick object at 0x02AD47B0>]

# plt.plot([1,2,3,4], [1,4,9,16])
# locs, labels = plt.xticks([1,2,3,4], ['Frogs','Hogs','Bogs','Slogs'])
# plt.setp(labels, 'rotation', 'vertical')
# plt.savefig('ticks_simpler')








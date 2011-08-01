"""A simple demo that uses Matplotlib and NumPy.

This combination provides a Python-based environment similar to the Matlab or
IDL consoles.

IPython with the -pylab option automatically detects the Matplotlib GUI backend
and adjusts to its event loop.  In addition to Tk, which Python handles
automatically, this works with GTK, WX, Qt3 and Qt4."""

import itertools

from matplotlib.patches import Ellipse

import numpy as N
import pylab as P

# <demo> stop
P.figure()

c = itertools.cycle(['blue','green','red'])

angles = N.linspace(0,135,4)  # degrees
ells = [Ellipse((1, 1), 4, 2, a,fc=c.next(),alpha=0.3) for a in angles]

a = P.subplot(111, aspect='equal')

for e in ells:
    e.set_clip_box(a.bbox)
    a.add_artist(e)

P.xlim(-2, 4)
P.ylim(-1, 3)
P.title('Antialiasing and transparency')

P.show()
# <demo> stop

P.figure()

t = N.linspace(0,3,200)
f = N.sin(N.pi*t)
g = N.sin(2*N.pi*t)
h = N.sin(3*N.pi*t)

P.title('Plots of many types...')
P.fill(t,f,'blue', alpha=0.3)
P.plot(t,g,'r^')
P.plot(t,h,'g-')

# Don't forget a show() call at the end of the script
P.show()

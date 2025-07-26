# This is part a collection of Python code to create animations based on the
# Mathematica code posted by @yuruyurau in X.com. The code by yuruyurau was
# converted to Python using ChatGPt and Co-pilot. Please give the full credit to yuruyurau.
# This code creates mesmerizing animations of sea-like creatures from a
# combination of mathematical functions.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 10000
x_vals = np.arange(N, 0, -1)
y_vals = x_vals / 235.0

def compute_points(t):
	x = x_vals
	y = y_vals
	k = (4 + np.cos(x / 9 - t)) * np.cos(x / 30)
	e = y / 7 - 13
	d = np.hypot(k, e) + np.sin(y / 99 + t / 2) - 4
	c = d - t
	q = 3 * np.sin(k * 2) + np.sin(y / 29) * k * (9 + 2 * np.sin(np.cos(e) * 9 - d * 4 + t))
	xp = q + 40 * np.cos(c) + 200
	yp = q * np.sin(c) + d * 35
	return xp, yp

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(6.5, 6.5))
xp0, yp0 = compute_points(0)
sc = ax.scatter(xp0, yp0, s=1, color='white', alpha=0.4)
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
ax.invert_yaxis()
ax.axis('off')

def animate(frame):
	t = frame * np.pi / 120
	x, y = compute_points(t)
	sc.set_offsets(np.c_[x, y])
	return sc,

ani = FuncAnimation(fig, animate, frames=180, interval=30, blit=True)
plt.show()
# Save the animation as an mp4 file
ani.save('yuruyurau4.gif', writer='pillow', fps=30)

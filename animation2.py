# This is part a collection of Python code to create animations based on the
# Mathematica code posted by @yuruyurau in X.com. The code by yuruyurau was
# converted to Python using ChatGPt and Co-pilot. Please give the full credit to yuruyurau.
# This code creates mesmerizing animations of sea-like creatures from a
# combination of mathematical functions.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

i_vals = np.arange(9999, -1, -1)
y_vals = i_vals / 235.0

def compute_points(t):
    x = i_vals
    y = y_vals
    k = (4 + np.sin(x / 11 + 8 * t)) * np.cos(x / 14)
    e = y / 8 - 19
    d = np.sqrt(k**2 + e**2) + np.sin(y / 9 + 2 * t)
    q = 2 * np.sin(2 * k) + np.sin(y / 17) * k * (9 + 2 * np.sin(y - 3 * d))
    c = d**2 / 49 - t
    xp = q + 50 * np.cos(c) + 200
    yp = q * np.sin(c) + d * 39 - 440
    return xp, 400 - yp, q

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(5.5, 5.5))
xp0, yp0, c0 = compute_points(0)
norm = plt.Normalize(c0.min(), c0.max())
colors = plt.cm.viridis(norm(c0))
sc = ax.scatter(xp0, yp0, s=2, color=colors, alpha=0.9)
ax.set_xlim(70, 330)
ax.set_ylim(30, 350)
ax.axis('off')

def animate(frame):
    t = frame / 60.0  # adjust speed here
    x, y, c = compute_points(t)
    colors = plt.cm.viridis(norm(c))
    sc.set_offsets(np.c_[x, y])
    sc.set_color(colors)
    return sc,

ani = FuncAnimation(fig, animate, frames=180, interval=30, blit=True)
plt.show()

# Save the animation as a GIF
ani.save("yuruyurau2.gif", writer='pillow', fps=30)

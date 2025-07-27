# This is part a collection of Python code to create animations based on the
# Javascript code posted by @yuruyurau in X.com. The code by yuruyurau was
# converted to Python using ChatGPt and Co-pilot. Please give the full credit to yuruyurau.
# This code creates mesmerizing animations of sea-like creatures from a
# combination of mathematical functions.


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

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
    return xp, 400 - yp

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(5.5, 5.5))
xp0, yp0 = compute_points(0)
sc = ax.scatter(xp0, yp0, s=1, color='white', alpha=0.4)
ax.set_xlim(70, 330)
ax.set_ylim(30, 350)
ax.axis('off')

def animate(frame):
    t = frame / 60.0  # adjust speed here
    x, y = compute_points(t)
    sc.set_offsets(np.c_[x, y])
    return sc,

parser = argparse.ArgumentParser(description="Animate sea-like creatures.")
parser.add_argument('--frames', type=int, default=180, help='Number of animation frames')
parser.add_argument('--gif', action='store_true', help='Save animation as GIF')
parser.add_argument('--mp4', action='store_true', help='Save animation as MP4')
args = parser.parse_args()

ani = FuncAnimation(fig, animate, frames=args.frames, interval=30, blit=True)
plt.show()

if args.gif or (not args.mp4):
	ani.save('yuruyurau1.gif', writer='pillow', fps=30)
if args.mp4:
	ani.save("yuruyurau1.mp4", writer="ffmpeg", fps=30)

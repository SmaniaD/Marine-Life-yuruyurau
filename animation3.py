# This is part a collection of Python code to create animations based on the
# Javascript code posted by @yuruyurau in X.com. The code by yuruyurau was
# converted to Python using ChatGPt and Co-pilot. Please give the full credit to yuruyurau.
# This code creates mesmerizing animations of sea-like creatures from a
# combination of mathematical functions.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

N = 10000
x_vals = np.arange(N, 0, -1)
y_vals = x_vals / 235.0

def compute_points2(t):
    x = x_vals
    y = y_vals
    k = (4 + np.sin(y * 2 - t) * 3) * np.cos(x / 29)
    e = y / 8 - 13
    d = np.hypot(k, e)
    c = d - t
    q = (3 * np.sin(k * 2) + 0.3 / (k + 1e-8) + np.sin(y / 25) * k * (9 + 4 * np.sin(e * 9 - d * 3 + t * 2)))
    xp = q + 30 * np.cos(c) + 200
    yp = q * np.sin(c) + d * 39 - 220
    return xp, yp

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(6.5, 6.5))
xp0, yp0 = compute_points2(0)
sc = ax.scatter(xp0, yp0, s=1, color='white', alpha=0.4)
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
ax.invert_yaxis()
ax.axis('off')

def animate(frame):
    t = frame * np.pi / 240
    x, y = compute_points2(t)
    sc.set_offsets(np.c_[x, y])
    # Show credits only in the first 2 seconds (i.e., first 60 frames at 30 fps)
    if frame < 60:
        if not hasattr(animate, "credit_text"):
            animate.credit_text = fig.text(
                0.01, 0.01,
                "Credit: based on code by @yuruyurau (X.com)",
                color='white',
                fontsize=8,
                ha='left',
                va='bottom',
                alpha=0.7
            )
        else:
            animate.credit_text.set_visible(True)
    else:
        if hasattr(animate, "credit_text"):
            animate.credit_text.set_visible(False)
    return sc,

parser = argparse.ArgumentParser(description="Animate sea-like creatures.")
parser.add_argument('--frames', type=int, default=180, help='Number of animation frames')
parser.add_argument('--gif', action='store_true', help='Save animation as GIF')
parser.add_argument('--mp4', action='store_true', help='Save animation as MP4')
args = parser.parse_args()

ani = FuncAnimation(fig, animate, frames=args.frames, interval=30, blit=True)

if args.gif or (not args.mp4):
    ani.save('yuruyurau3.gif', writer='pillow', fps=30)
if args.mp4:
    ani.save("yuruyurau3.mp4", writer="ffmpeg", fps=30)
plt.show()    

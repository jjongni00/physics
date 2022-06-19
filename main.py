import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
import time

xSize = 100
ySize = 100
pointCount = 2

plane = np.zeros((xSize, ySize))
point = np.array([[20, 20], [80, 80]])
dist = np.zeros(pointCount)
timePhase = 2
xRaw = np.zeros(xSize * ySize)
yRaw = np.zeros(xSize * ySize)
zRaw = np.zeros(xSize * ySize)


def calc():
  global dist, plan, xSize, ySize, pointCount, timePhase, xRaw, yRaw, zRaw, plane
  plane = np.zeros((xSize, ySize))
  for x in range(0, xSize):
    for y in range(0, ySize):
      for p in range(0, pointCount):
        dist[p] = math.sqrt(pow(point[p][0] - x, 2) + pow(point[p][1] - y, 2))
        if dist[p] <= timePhase:
          plane[x][y] += math.sin(dist[p] * 0.5 + timePhase)

  for x in range(0, xSize):
    for y in range(0, ySize):
      xRaw[x * xSize + y] = x
      yRaw[x * xSize + y] = y
      zRaw[x * xSize + y] = plane[x][y]

#plt.ion()
fig = plt.figure(figsize=(10, 10))
gp = fig.add_subplot(projection='3d')
gp.set_xlim([0, xSize])
gp.set_ylim([0, ySize])
gp.set_zlim([-10, 10])
gp.view_init(40,60)
ctx = gp.scatter(xRaw, yRaw, zRaw, c=zRaw, cmap="inferno")
plt.draw()

def animate(i):
  global ctx, timePhase
  timePhase += 0.5
  calc()
  ctx.remove()
  ctx = gp.scatter(xRaw, yRaw, zRaw, c=zRaw, cmap="inferno")

anim = animation.FuncAnimation(fig, animate, interval=20)
anim.save("test.mp4")
plt.show()
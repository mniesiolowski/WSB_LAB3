import matplotlib.pyplot as plot
import numpy as np
import random

n = int(input("Podaj n: "))

x = [round(random.uniform(0, 1), 2) for _ in range(n)]
y = [round(random.uniform(0, -1), 2) for _ in range(n)]
index = np.arange(n)

fig, ax = plot.subplots()
barX = ax.bar(index, x, 0.3, color="blue")
barY = ax.bar(index, y, 0.3, color="red")
offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
for rect in barX:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() * offset['center'], 1.01 * height,
            '{}'.format(height), ha='center', va='bottom')
for rect in barY:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() * offset['center'], 1.01 * height,
            '{}'.format(height), ha='center', va='bottom')
plot.show()
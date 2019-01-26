import pylab
import matplotlib.pyplot as plt
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
x = pylab.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

y2 = [i**2 / 3 for i in x if i >= 0]

x1 = [i for i in x if i <= 0]
x2 = [i for i in x if i >= 0]

pylab.plot(x1, y1, x2, y2)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()

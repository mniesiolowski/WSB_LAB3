import matplotlib.pyplot as plt
import pylab as p


a=float(input("Podaj a = "))
b=float(input("Podaj b = "))

x=p.arange(-10, 10, 1)
y=a*x +b

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres f(x) = a*x +b")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

if a > 0:
    plt.text(5, 5, "Funkcja rosnąca")
elif a < 0:
    plt.text(-10, 5, "Funkcja malejąca")
elif a == 0:
    plt.text(3, b, "Funkcja stała")

plt.legend(["Funckja liniowa"])
plt.grid(True)
plt.show()

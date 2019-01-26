import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input("Ile ruchów? "))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):
    # wylosuj k¹t i zamieñ go na radiany
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)  # wylicz wspó³rzêdn¹ x
    y = y + np.sin(rad)  # wylicz wspó³rzêdn¹ y
    # print(x, y)
    lx.append(x)
    ly.append(y)

print(lx, ly)

# oblicz wektor koñcowego przesuniêcia
s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesuniêcia:", s)
plt.plot((0, lx[-1]), (0, ly[-1]), color="blue")
plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("lx")
plt.ylabel("ly")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()

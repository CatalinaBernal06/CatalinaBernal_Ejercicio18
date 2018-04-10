import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos.txt')
x = datos[:,0]
y = datos[:,1]
h = 0.1
N = 3/h
xr = np.linspace(0, 3, N )
yr = np.exp(-xr)

plt.figure()
plt.scatter(x, y)
plt.plot(xr, yr)
plt.savefig('ecu.pdf')

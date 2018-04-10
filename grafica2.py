import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos2.txt')
x = datos[:,0]
y = datos[:,1]
z = datos[:, 2]

h = 0.1
N = 10/h
xr = np.linspace(0, 10, N )
yr = np.cos(xr)

plt.figure()
plt.scatter(x, y)
plt.plot(xr, yr)
plt.savefig('ecu2.pdf')

plt.figure()
plt.plot(y, z, label='der')
plt.savefig('proof.pdf')

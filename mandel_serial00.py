#!/usr/bin/python3
#runs on RPI, no commandline input, no *.png output
#if chmod 755, then
#./mandel_serial00.py 
import timeit
def mandelbrot(x, y, maxit):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < maxit:
        z = z**2 + c
        it += 1
    return it

x1, x2 = -2.0, 1.0
y1, y2 = -1.0, 1.0
w, h = 120, 100
maxit = 256

start_time=timeit.default_timer()
import numpy
C = numpy.zeros([h, w], dtype='i')
dx = (x2 - x1) / w
dy = (y2 - y1) / h
for i in range(h):
    y = y1 + i * dy
    for j in range(w):
        x = x1 + j * dx
        C[i, j] = mandelbrot(x, y, maxit)
print("cpu time = " + str(timeit.default_timer()-start_time) + ' micro seconds')

#from matplotlib import pyplot
#pyplot.imshow(C, aspect='equal')
#pyplot.spectral()
#pyplot.show()
        
import matplotlib.pyplot as plt
plt.imshow(C, aspect='equal', cmap='nipy_spectral_r')
#plt.brg()
plt.show()

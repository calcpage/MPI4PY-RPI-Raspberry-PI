#!/usr/bin/python3
#mandel_serial03.py 
#works with commandline arguments on RPI
#output *.png file
#if chmod 755:
#./mandel_serial03.py hort vert colors
import sys
import timeit
print('len(sys.argv) = ' + str(len(sys.argv)))
print('sys.argv[0] = ' + sys.argv[0])
w, h, maxit = sys.argv[1], sys.argv[2], sys.argv[3]
print('w = ' + w)
print('h = ' + h)
print('maxit = ' + maxit)

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
#w, h = 150, 100
#maxit = 127
w = int(w)
h = int(h)
maxit = int(maxit)

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
		

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#pyplot.imshow(C, aspect='equal')
#pyplot.spectral()
#pyplot.show()
plt.imshow(C, aspect='equal', cmap='nipy_spectral_r')
plt.savefig("mandelbrot.png", dpi=200)

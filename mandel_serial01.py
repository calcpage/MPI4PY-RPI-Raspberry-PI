#mandel_serial01.py
#Works in SAGE without command arguments
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
w, h = 150, 100
maxit = 128

ans=""
import numpy
C = numpy.zeros([h, w], dtype='i')
dx = (x2 - x1) / w
dy = (y2 - y1) / h
for i in range(h):
    y = y1 + i * dy
    ans+="\n"
    for j in range(w):
        x = x1 + j * dx
        num = mandelbrot(x, y, maxit)
        C[i, j] = num
        ans+=str(num)

print(ans)   
     
from matplotlib import pyplot
pyplot.imshow(C, aspect='equal')
#pyplot.spectral()
pyplot.show()

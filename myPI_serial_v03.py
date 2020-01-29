#MrG 2020.0116 What Is A Right Right Riemann Sum
#Version03: python myPI_serial_v03.py a b n
#Version03: with timeit, commandline input & error
import timeit
import sys
import math

def f(x):
	return 4.0/(1+x**2)

def Rsum(a,b,n):
    area=0.0
    for i in range(n):
        area=area+(b-a)/n*f(a+(b-a)/n*(i+1))
    return area

a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])
print("file name = " + sys.argv[0])
print("num args = " + str(len(sys.argv)))
print("a = " + str(a))
print("b = " + str(b))
print("n = " + str(n))
print("")

start_time = timeit.default_timer()
myPI = Rsum(a,b,n)
end_time = timeit.default_timer()
error = myPI-math.pi

print("pi   = " + str(math.pi))
print("area = " + str(myPI))
print("error = " + str(error))
print("start_time = " + str(start_time))
print("end_time   = " + str(end_time))
print("elapsed time = " + str(end_time-start_time) + ' seconds')
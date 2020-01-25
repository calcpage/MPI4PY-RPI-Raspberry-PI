#MrG 2020.0116 What Is A Right Right Riemann Sum
#Version02: python myPI_serial_v02.py
#Version02: with timeit
import timeit

def f(x):
	return 4.0/(1+x**2)

def Rsum(a,b,n):
    area=0.0
    for i in range(n):
        area=area+(b-a)/n*f(a+(b-a)/n*(i+1))
    return area

pi = str(Rsum(0.0,1.0,100))
start_time = timeit.default_timer()
end_time = timeit.default_timer()

print("area = " + pi)
print("start_time = " + str(start_time))
print("end_time = " + str(end_time))
print("elapsed time = " + str(end_time-start_time))

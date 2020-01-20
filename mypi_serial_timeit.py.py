#!/usr/bin/python
#MrG 2020.0116 What Is A Right Right Riemann Sum
import timeit

def f(x):
    return 4.0/(1+x**2)
	
def Rsum(a,b,n):
    area=0.0
    for i in range(n):
        area=area+(b-a)/n*f(a+(b-a)/n*(i+1))
    return area

start_time=timeit.default_timer()
print "area = " + str(Rsum(0.0,1.0,4000000))
print "cpu time = " + str(timeit.default_timer()-start_time) + ' micro seconds'
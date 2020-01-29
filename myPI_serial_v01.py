#MrG 2020.0116 What Is A Right Right Riemann Sum
#Version01: python myPI_serial_v01.py
#Version01: just find the area!
def f(x):
	return 4.0/(1+x**2)

def Rsum(a,b,n):
    area=0.0
    for i in range(n):
        area=area+(b-a)/n*f(a+(b-a)/n*(i+1))
    return area

print("area = " + str(Rsum(0.0,1.0,10000)))
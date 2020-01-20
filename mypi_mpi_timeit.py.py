#!/usr/bin/python
#mpirun -np 4 ./myPI_MPI.py
from mpi4py import MPI
import math, timeit

def compute_pi(n, start=0, step=1):
    h=1.0/n
    s=0.0
    for i in range(start, n, step):
        x=h*(i+0.5)
        s+=4.0/(1.0+x**2)
    return s*h

comm=MPI.COMM_WORLD
nprocs=comm.Get_size()
myrank=comm.Get_rank()

if myrank==0:
    n=4000000
    start_time=timeit.default_timer()
else:
    n=None
    
n=comm.bcast(n, root=0)
mypi=compute_pi(n,myrank,nprocs)
pi=comm.reduce(mypi,op=MPI.SUM,root=0)

if myrank==0:
    rel_error=pi-math.pi
    abs_error=abs(rel_error)
    print('pi   = ' + str(math.pi))
    print('area = '+ str(pi))
    print('relative error = '+ str(rel_error))
    print('cpu time = ' + str(timeit.default_timer()-start_time) + ' micro seconds')
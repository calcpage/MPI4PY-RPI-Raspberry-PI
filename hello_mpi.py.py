#!/usr/bin/python
#to execute: mpirun -np 4 python hello_mpi.py (does not require: #!/usr/bin/python)
#or
#chmod 755 hello_mpi.py
#to execute: mpirun -np hello_mpi.py (requires: chmod & #!/usr/bin/python)
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
print 'rank = ' + str(rank) + ' of ' + str(size) + '!'
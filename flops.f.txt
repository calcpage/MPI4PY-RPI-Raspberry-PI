c
c  flops.f
c
c  Author:
c       Yuri Sbitnev <yuri@linux-ekb.info>
c
c  Copyright (c) 2008-2009 Yuri Sbitnev
c
c  This program is free software; you can redistribute it and/or modify
c  it under the terms of the GNU General Public License as published by
c  the Free Software Foundation; either version 2 of the License, or
c  (at your option) any later version.
c
c  This program is distributed in the hope that it will be useful,
c  but WITHOUT ANY WARRANTY; without even the implied warranty of
c  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
c  GNU General Public License for more details.
c
c  You should have received a copy of the GNU General Public License
c  along with this program; if not, write to the Free Software
c  Foundation, Inc., 59 Temple Place, Suite 330, Boston, 
c  MA 02111-1307 USA


      program calc_mflops
      include 'mpif.h'
      integer i, j, n
      double precision w, gsum, sum
      double precision v
      integer np, myid, ierr, niter, status(MPI_STATUS_SIZE)
      real*8 time, amflops, amflops1, time1, time2, dsecnd 
      integer mflops, mflops1
c Initialize MPI. Find number of processors.
      call MPI_INIT( ierr )
      call MPI_COMM_RANK( MPI_COMM_WORLD, myid, ierr )
      call MPI_COMM_SIZE( MPI_COMM_WORLD, np, ierr ) 
c Zero process determines the number of points.
      if ( myid .eq. 0 ) then
      n = 200000000
      endif 

      time1 = MPI_Wtime()

c Send number of point from zero process to all other processes
      call MPI_BCAST(n, 1, MPI_INTEGER, 0, MPI_COMM_WORLD, ierr)
c Calculate partial sum
      w = 1.0 / n

      do j = 1, 4
      sum = 0.0d0
      do i = myid+1, n, np
      v = (i - 0.5d0 ) * w
      v = 4.0d0 / (1.0d0 + v * v)
      sum = sum + v
      end do 
      end do
c Summarize the partial sums and store it in zero process
      call MPI_REDUCE(sum, gsum, 1, MPI_DOUBLE_PRECISION,
     $                MPI_SUM, 0, MPI_COMM_WORLD, ierr)

      time2 = MPI_Wtime()
      time   = (time2 - time1) / 4

      niter = 0
      do i = myid+1, n, np
      niter = niter + 1
      end do 

      mflops1 = 9 * niter / (1000000.0 * time)

c Zero process prints cluster benchmark results
      if (myid .eq. 0) then
      mflops = 9 * n / (1000000.0 * time)
      print *, '   '
      print '(A)', '  HPC Test ----------------------------------------'
      print '(A,I2.1)', '  Quantity of processors =  ', np
      print '(A,F6.2,A)', 
     $'  Calculation time       = ', time, ' seconds'
      print '(A,I6.1,A)', 
     $'  Cluster speed          = ', mflops, ' MFLOPS'
      print '(A)', '  -------------------------------------------------'
      print '(A,I2.2,A,I6.1,A)', 
     $'  Cluster node N',0,' speed = ', mflops1, ' MFLOPS'
c Collect and print benchmark results from individual processes
      do i = 1, np-1
      CALL MPI_RECV(mflops1, 1, MPI_REAL8, i, 0, 
     $              MPI_COMM_WORLD, status, ierr)
      print '(A,I2.2,A,I6.1,A)', 
     $'  Cluster node N', i, ' speed = ', mflops1, ' MFLOPS'
      end do
      print '(A)', '  -------------------------------------------------'
      print *, '   '
      else
c Send local process benchmark result to zero process
      call MPI_SEND(mflops1, 1, MPI_REAL8, 0, 0,
     $               MPI_COMM_WORLD, ierr)
      endif 

c Close MPI
      call MPI_FINALIZE(ierr)
      end
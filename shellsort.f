c----------------------------------------------------------------------c
      subroutine shellsort(x,n,ind)
c     Donald Shell's sorting algorithm (1959) 304.8 APPL.STATIST.      c
c     (1996), VOL.45, No.3 sort the n values stored in array X in      c
c     ascending order. The original program from NIST's webpage is     c
c     modified such that the index of original array is also saved in  c
c     the order of its 'ascending' value                               c
      implicit none
      integer n, i, j, incr, itemp, ind(n)
      real*8 x(n), temp

cf2py intent(in,out) x, n, ind
      itemp = -1000             ! yj
      incr = 1
c     Loop : calculate the increment

      do i=1, n
         ind(i) = i
      enddo

 10   incr = 3 * incr + 1
      if (incr.le.n) goto 10
c     Loop: Shell - Metzner sort
 20   incr = incr / 3
      i = incr + 1
 30   if(i.gt.n) goto 60
      temp = x(i)
      itemp = ind(i)
      j = i
 40   if (x(j - incr).lt.temp) goto 50
      x(j) = x(j - incr)        ! x assignment
      ind(j) = ind(j - incr)
      j = j - incr
      if (j.gt.incr) goto 40
 50   x(j) = temp               ! x assignment
      ind(j) = itemp
      i = i + 1
      goto 30
 60   if (incr.gt.1) goto 20

      return
      end subroutine shellsort  ! end of subr. shellsort

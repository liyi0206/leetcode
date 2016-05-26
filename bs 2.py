#I. operation design (*) - bit manipulation
#29. Divide Two Integers - no multiplication/division/mod, so only bit manipulation/plus/minus/abs
# edge case: dividend==divisor, n=0, but still need to do dividend-=divisor and res+=1<<n

class Solution(object):
    def divide(self, dividend, divisor):
        import sys
        if divisor==0: return sys.maxint
        sign=-1 if (dividend<0)^(divisor<0) else 1
        dividend,divisor=abs(dividend),abs(divisor)
        n=0
        while (dividend>>1)>=divisor:
            divisor<<=1
            n+=1
            
        res=0
        while n>=0:
            if divisor<=dividend:
                dividend-=divisor
                res+=(1<<n)
            n-=1
            divisor>>=1  
             
        return res*sign

a=Solution()
print a.divide(380,26) #14
print a.divide(0,1)
print a.divide(1,1)

#50. Pow(x, n)
#69. Sqrt(x)


#II. divide and conquer
#4. [D] Median of Two Sorted Arrays (*) - time o(log(m+n))



#240.[D] Search a 2D Matrix II (*)


#III, BST
#315 Count of Smaller Numbers After Self
#327 Count of Range Sum ()
#220 Contains Duplicate III (*) - solved in Java, as python has no BST implementation


#218. the skyline problem
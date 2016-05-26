# all use recursion
# quick sort
def quickSort(nums):
    N = len(nums)
    if N<=1: return nums

    # could shuffle nums first, to reduce possibility of worst cases
    # partitioning, choose a pivot nums[-1]. 
    # idx p is the right boundary of all nums smaller than pivot **
    # for all numbers, if <nums[-1], switch with p
    p = 0 # two pointers, p (slower) and i (faster)
    for i in range(N-1):
        if nums[i]<nums[-1]:  #####
            nums[p],nums[i] = nums[i],nums[p]   ####
            p+=1  #####
    
    # at last to put pivot to p
    nums[p],nums[-1] = nums[-1],nums[p]

    nums[:p] = quickSort(nums[:p])
    nums[p+1:]=quickSort(nums[p+1:])
    return nums
    
# quick select - find kth smallest
import random
def quickSelect(nums,K):
    N = len(nums)
    if N<K: return None
    
    # we think it is equivalent to shuffle and choose idx -1
    # from the avoiding worst case point, they are equivalent
    pivIdx = random.randint(0,N-1)
    nums[-1],nums[pivIdx] = nums[pivIdx],nums[-1]
    
    p = 0
    for n in range(N-1):
        if nums[n]<nums[-1]:
            nums[n],nums[p] = nums[p],nums[n]        
            p+=1
    nums[-1],nums[p] = nums[p],nums[-1]

    # K is the 0 based k
    if p>K: return quickSelect(nums[:p],K)
    elif p<K: return quickSelect(nums[p+1:],K-p-1)
    else: return nums[p]
    
# merge sort
def mergeSort(nums):
    N = len(nums)
    if N<=1: return nums

    nums[:N/2] = mergeSort(nums[:N/2])
    nums[N/2:] = mergeSort(nums[N/2:])

    # merege
    # need o(n) extra space, for copy
    cp0,cp1 = nums[:N/2],nums[N/2:]
    i0,i1 = 0,0
    for i in range(N):
        if i1>=len(cp1) or (i0<len(cp0) and cp0[i0]<cp1[i1]):
           nums[i]=cp0[i0]
           i0+=1
        else:
           nums[i]=cp1[i1]
           i1+=1
    return nums
    
x = [4,6,3,2,1,9,7,5,8]
print quickSelect(x,7)
print quickSort(x)
print mergeSort(x)
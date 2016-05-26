#I. Basics
#23. Merge k Sorted Lists (*)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self,lists):
        import heapq
        heap=[]
        for a in lists:
            if a: heapq.heappush(heap,(a.val,a))
        dummy=ListNode(0)
        cur=dummy
        while heap:
            a=heapq.heappop(heap)
            node=a[1]
            tmp=node.next
            cur.next=node
            cur=cur.next
            if tmp: heapq.heappush(heap,(tmp.val,tmp))
        return dummy.next
            
l1=ListNode(1)
l1.next=ListNode(3)
l1.next.next=ListNode(5)
l1.next.next.next=ListNode(7)

l2=ListNode(2)
l2.next=ListNode(8)
l2.next.next=ListNode(9)

l3=ListNode(4)
l3.next=ListNode(6)
l3.next.next=ListNode(10)

a=Solution()
l=a.mergeKLists([l1,l2,l3])
cur = l
while cur:
    print cur.val,
    cur=cur.next

#215. Kth Largest Element in an Array (*) - heap queue or quick select
#pay attention to the same value numbers of the random number


#295. Find Median from Data Stream (*) - two heapq, one for larger half numbers, one for smaller half numbers



#II, Ugly numbers
#263. Ugly Number - warm up
#264. Ugly Number II - DP enough



#313. Super Ugly Number (*) - extend from ugly number II, 
#use heapq to get min from primes[i]*res[idx[i]]. 
#trick: multiple min from different idx. point: timeout if rebuild heapq each time. 
#solution: each time pop one value, update idx for that value, and push new value to heapq. 
#if m==res[-1] then don't append.
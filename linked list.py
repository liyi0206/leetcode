# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#I. Basics - in place
#19. Remove Nth Node From End of List
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        fast,slow=dummy,dummy
        for i in range(n): 
            fast=fast.next
        while fast.next:
            fast,slow=fast.next,slow.next
        slow.next=slow.next.next
        return dummy.next

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
  
#a=Solution()
#new = a.removeNthFromEnd(head,2)
#cur=new
#for i in range(4):
#    print cur.val
#    cur=cur.next

#61. Rotate List
# if k%n==0, then no need to move
# otherwise slow.next is None, so dummy.next=None
class Solution(object):
    def rotateRight(self,head,k):
        if not head: return None
        cur,n=head,0
        while cur:
            cur=cur.next
            n+=1
        k=k%n
        if k==0: return head
        
        dummy=ListNode(0)
        dummy.next=head
        fast,slow=dummy,dummy
        for i in range(k): 
            fast=fast.next
        while fast.next:
            fast,slow=fast.next,slow.next
        
        tmp=slow.next
        slow.next=None
        dummy.next=tmp
        fast.next=head
        
        return dummy.next
        
#a=Solution()
#new = a.rotateRight(head,2)
#cur=new
#for i in range(5):
#    print cur.val
#    cur=cur.next

#new= a.rotateRight(ListNode(1),1)
#print new.val

#83. Remove Duplicates from Sorted List
class Solution(object):
    def deleteDuplicates(self,head):
        if not head: return None
        cur=head
        while cur.next:
            if cur.next.val==cur.val:
                cur.next=cur.next.next
            else: cur=cur.next
        return head
  
head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(3)
      
#a=Solution()
#new= a.deleteDuplicates(head)
#cur=new
#for i in range(3):
#    print cur.val
#    cur=cur.next

#82. Remove Duplicates from Sorted List II
class Solution(object):
    def deleteDuplicates(self,head):
        if not head: return None
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        while cur.next and cur.next.next:
            if cur.next.next.val==cur.next.val:
                tmp=cur.next.next
                while tmp.next and tmp.next.val==tmp.val:
                    tmp=tmp.next
                cur.next=tmp.next
            else: cur=cur.next
        return dummy.next
        
#a=Solution()
#new= a.deleteDuplicates(head)
#print new.val
#print

head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(1)
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(3)
      
#a=Solution()
#new= a.deleteDuplicates(head)
#cur=new
#for i in range(2):
#    print cur.val
#    cur=cur.next

#86. Partition List (*) - in place is tricky
# remember to add right.next=None at last !
class Solution(object):
    def partition(self, head, x):
        if not head: return None
        left_dummy,right_dummy=ListNode(0),ListNode(0)
        cur,left,right=head,left_dummy,right_dummy
        while cur:
            if cur.val<x: 
                left.next=cur
                left=left.next
            else:
                right.next=cur
                right=right.next
            cur=cur.next
        right.next=None
        left.next=right_dummy.next
        return left_dummy.next

head=ListNode(1)
head.next=ListNode(4)
head.next.next=ListNode(3)
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(2)
      
#a=Solution()
#new= a.partition(head,3)
#cur=new
#for i in range(6):
#    print cur.val
#    cur=cur.next

#143. Reorder List (*) - based on reverse list, reverse the latter half


#203. Remove Linked List Elements
#234. Palindrome Linked List - based on reverse list, return true/false
#237. Delete Node in a Linked List - from node, change value, link to next
#328. Odd Even Linked List

#II. reverse list
#First one similar to last one, but not reverse.
#24 Swap Nodes in Pairs



#206. Reverse Linked List *****
class SolutionIter(object):
    def reverseList(self, head):
        if not head: return None
        dummy=ListNode(0)
        dummy.next=head
        
        cur=dummy
        front=None
        while cur.next:  
            tmp=cur.next
            cur.next=cur.next.next 
            tmp.next=front
            front=tmp
        return front
        
    def reverseList2(self,head):
        if not head: return None
        front=None
        while head: #head - cur
            tmp=head.next
            head.next=front #front - prev
            front=head
            head=tmp
        return front
            
class SolutionRecur(object): ##*********very important*********
    def reverseList(self,head):
        return self.recur(head,None)
        
    def recur(self,head,new): #old_list, new_list
        if not head: return new
        tmp=head.next
        head.next=new
        return self.recur(tmp,head)

#a=SolutionRecur()
#new= a.reverseList(head)
#cur=new
#for i in range(5):
#    print cur.val
#    cur=cur.next

#92. Reverse Linked List II
# need dummy, o/w when m is 1, it is wrong
class Solution(object):
    def reverseBetween(self,head,m,n):
        if not head: return None
        dummy=ListNode(0)
        dummy.next=head
        
        cur=dummy
        for i in range(m-1): cur=cur.next
        tail1=cur
        tail2,cur=cur.next,cur.next
        front=None
        for i in range(n-m+1):
            tmp=cur.next
            cur.next=front
            front=cur
            cur=tmp
        tail1.next=front
        tail2.next=cur
        return dummy.next

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

#a=Solution()
#new = a.reverseBetween(head,2,4)
#cur=new
#for i in range(5):
#    print cur.val
#    cur=cur.next

#a=Solution()
#new = a.reverseBetween(ListNode(5),1,1)
#print new.val

#25. Reverse Nodes in k-Group (*)
class Solution(object):
    def reverseKGroup(self,head,k):
        if not head: return None
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        n=0
        while cur:
            front=None
            for i in range(k):
                tmp=cur.next
                cur.next=front
                front=cur
                cur=tmp    
        
a=Solution()
new = a.reverseKGroup(head,2)
cur=new
for i in range(5):
    print cur.val
    cur=cur.next
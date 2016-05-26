#206
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head: return None
        prev=head
        cur=head.next
        while cur:
            tmp=cur.next
            cur.next=prev
            head.next=tmp
            prev=cur
            cur=tmp
        return prev
    
    def reverseList2(self, head):
        if not head: return None
        prev=None
        cur=head
        while cur:
            tmp=cur.next
            cur.next=prev
            #head.next=tmp
            prev=cur
            cur=tmp
        return prev
        
#pow(x,n)
class Solution(object):
    def myPow(self, x, n):
        pass
        
# 218. The Skyline Problem
class Solution(object):
    def getSkyline(self, buildings):
        heights=[]
        for left,right,h in buildings:
            heights.append((left,-h))
            heights.append((right,h))
        heights.sort()
        
        prev=0
        queue=[0] # for h
        res=[]
        for loc,h in heights:
            if h<0: queue.append(-h)
            else: queue.remove(h)
            cur=max(queue)
            
            if cur!=prev:
                res.append((loc,cur))
                prev=cur
        return res
        
#a=Solution()
#print a.getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]])
#[[2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]]

#271. Encode and Decode Strings
class Codec:
    def encode(self, strs):
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        print res
        return res
       
    def decode(self,s):
        res=[]
        cur=0
        while cur<len(s):
            loc=s.find("#",cur)
            length=int(s[cur:loc])
            string=s[loc+1:loc+1+length]
            res.append(string)
            cur=loc+1+length
        return res

#strs=["hello world!","the sky is blue"]
#codec = Codec()
#print codec.decode(codec.encode(strs))
#'12:hello world!15:the sky is blue'

#297. Serialize and Deserialize Binary Tree
## need to serialize using comma, o/w multiple digit number, negtive number
## are hard to be parsed.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Codec:
    def serialize(self,root):
        #self.res=""
        self.res=[]
        self.recur1(root)
        return ",".join(self.res) #self.res
    def recur1(self,node): #preorder traversal
        if node:
            #self.res+=str(node.val)
            self.res.append(str(node.val))
            self.recur1(node.left)
            self.recur1(node.right)
        else:
            #self.res+="#"
            self.res.append("#")
        
    def deserialize(self, data):
        #self.vals=list(data)
        self.vals=data.split(",")
        root=self.recur2()
        return root
    def recur2(self):
        val=self.vals.pop(0)
        if val!="#":
            node=TreeNode(int(val))
            node.left=self.recur2()
            node.right=self.recur2()
            return node
        else: return None
        
#root=TreeNode(1)
#root.left =TreeNode(2)
#root.right=TreeNode(3)
#root.right.left =TreeNode(4)
#root.right.right=TreeNode(5)

#codec = Codec()
#tmp = codec.serialize(root); print tmp
#new = codec.deserialize(tmp)
#print new.val,new.left.val,new.right.val,
#print new.left.left,new.left.right,
#print new.right.left.val,new.right.right.val

#298. Binary Tree Longest Consecutive Sequence
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0 ##o/w return 1 wrong
        self.res=0
        self.dfs(root,None,0)
        return self.res
        
    def dfs(self,node,prev,cnt):
        if not node: 
            self.res=max(self.res,cnt)
            return
        ### only if node exists
        if prev and prev.val+1==node.val: 
            self.dfs(node.left,node,cnt+1)
            self.dfs(node.right,node,cnt+1)
        else:
            self.res=max(self.res,cnt)
            self.dfs(node.left,node,1)
            self.dfs(node.right,node,1)    
            
#root1=TreeNode(1)
#root1.right=TreeNode(3)
#root1.right.left=TreeNode(2)
#root1.right.right=TreeNode(4)
#root1.right.right.right=TreeNode(5)
#            
#root2=TreeNode(2)
#root2.right=TreeNode(3)
#root2.right.left=TreeNode(2)
#root2.right.left.left=TreeNode(1)
#
#a=Solution()
#print a.longestConsecutive(root1) #3
#print a.longestConsecutive(root2) #2

#42. Trapping Rain Water
class Solution(object):
    def trap(self, height):
        if not height: return 0 ##o/w runtime error
        n=len(height)
        
        array1=[height[0]]
        for h in height[1:]:
            array1.append(max(array1[-1],h))
        #print array1
        
        array2=[height[-1]]
        for h in reversed(height[:-1]):
            array2.append(max(array2[-1],h))
        #print array2
        
        res=[]
        for i in range(n):
            res.append(max(min(array1[i],array2[n-i-1])-height[i],0)) ##
        #print res
        return sum(res)
            
#a=Solution()
#print a.trap([0,1,0,2,1,0,1,3,2,1,2,1])

#289. Game of Life
class Solution(object):
    def gameOfLife(self, board):
        pass

#318. Maximum Product of Word Lengths
class Solution(object):
    def maxProduct(self, words):
        bits=[0]*len(words)
        for i,word in enumerate(words):
            for c in word:
                idx=ord(c)-ord('a')
                bits[i]|=1<<idx # | not +, o/w aa will adds up to 10, while should be 01
        #for num in bits:
        #    print bin(num)[2:].zfill(26)
        res=0
        for i in range(len(bits)):
            for j in range(i+1,len(bits)):
                if bits[i]&bits[j]==0: 
                    #print words[i],words[j]
                    res=max(res,len(words[i])*len(words[j]))
        return res

#a=Solution()
#print a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) #16
#print a.maxProduct(["a","aa","aaa","aaaa"]) #0

#228. Summary Ranges
class Solution(object):
    def summaryRanges(self, nums):
        if not nums: return [] ## o/w runtime error
        res=[]
        cur=nums[0]
        nums.append(nums[-1]+2)
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if nums[i-1]==cur: res.append(str(cur))
                else: res.append(str(cur)+'->'+str(nums[i-1]))
                cur=nums[i]
        return res

#a=Solution()
#print a.summaryRanges([0,1,2,4,5,7]) #["0->2","4->5","7"]
#print a.summaryRanges([0,1,2,4,5,6])
#print a.summaryRanges([0,1,2,4,6,7])
#print a.summaryRanges([0])
#print a.summaryRanges([])
#print a.summaryRanges([-1])
    
#163. Missing Ranges
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        #if not nums: return [] ## don't need, as return ["lower->upper"]
        res=[]
        cur=lower
        nums.append(upper+1)
        for i in range(len(nums)):
            #if nums[i]>cur: ## don't need, as cur==nums[i] for the other case
                if nums[i]==cur+1: res.append(str(cur))
                elif nums[i]>cur+1:res.append(str(cur)+"->"+str(nums[i]-1))
                cur=nums[i]+1
            #else: cur=cur+1
        return res
        
#a=Solution()
#print a.findMissingRanges([0,1,3,50,75],0,99) #["2","4->49","51->74","76->99"]
#print a.findMissingRanges([-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000],-1000000000,1000000000)
#print a.findMissingRanges([],1,1) #1

#50. Pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        #if n==1: return x 
        if n==0: return 1 ## stop rule should cover 0
        if n<0: return 1.0/self.myPow(x,-n) ##1.0
        half=self.myPow(x,n/2)
        res=half*half
        if n%2: res=res*x
        return res
        
#a=Solution()
#print a.myPow(3,5) #243
#print a.myPow(3,0)
   
#57. Insert Interval
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object): ###idx<len(intervals) is needed for both while loops###
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval] ##o/w runtime error
        idx=0
        while idx<len(intervals) and intervals[idx].end<newInterval.start: idx+=1
        # 3 cases: new.s,new.e,idx.s,idx.e
        #          idx.s,new.s,new.e,idx.e
        #          idx.s,new.s,idx.e,new.e
        mergeInterval=Interval(newInterval.start,newInterval.end)
        i=idx
        while i<len(intervals) and not newInterval.end<intervals[i].start:
            mergeInterval.start=min(mergeInterval.start,intervals[i].start)
            mergeInterval.end=max(mergeInterval.end,intervals[i].end)
            i+=1
        return intervals[:idx]+[mergeInterval]+intervals[i:]

#a=Solution()
#res=a.insert([Interval(1,3),Interval(6,9)], Interval(2,5))
#for a in res: print a.start,a.end

#253. Meeting Rooms II
class Solution(object):
    def minMeetingRooms(self, intervals):
        times=[]
        for m in intervals:
            times.append((m.start,'s'))
            times.append((m.end,'e'))
        times.sort()
        
        res=0 # num_rooms
        cur=0
        for time,x in times:
            if x=="s": cur+=1
            else: cur-=1
            res=max(res,cur)
        return res
        
#a=Solution()
#print a.minMeetingRooms([Interval(0,30),Interval(5,10),Interval(15,20)]) #2
      
#10. Regular Expression Matching  
class Solution(object):
    def isMatch(self, s, p):
        dp=[[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0]=True
        #for i in range(1,len(s)): dp[i][0]=False
        
        ### need to be initialized, as there is no i-1
        ### remember to use len(p)+1 for dp range ###
        ### remember j>=2
        for j in range(1,len(p)+1): 
            if p[j-1]=="*" and j>=2: 
                dp[0][j]=dp[0][j-2]
                
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]!="*":
                    dp[i][j]=dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]==".")
                else:
                    dp[i][j]=(dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]==".")) \
                             or dp[i][j-2] ###
        #for l in dp: print l
        return dp[-1][-1]
  
#a=Solution()
#print a.isMatch("aab","c*a*b") #True

#44. Wildcard Matching   - too many edge cases = =
# try to match the next char after * as early as possible, 
# then there will be more options in s for the rest of p to match
# once meet the next *
class Solution(object):
    def isMatch(self, s, p):
        has_star=0
        ps,pp=0,0
        while ps<len(s):
            if pp<len(p) and (s[ps]==p[pp] or p[pp]=='?'):
                ps,pp=ps+1,pp+1
            elif pp<len(p) and p[pp]=='*':
                has_star=1
                pp+=1
                #while ps<len(s) and pp<len(p) and (s[ps]!=p[pp] and p[pp]!="?"): 
                #    ps+=1 ###won't work for the "**" case
                lasts,lastp=ps,pp
            elif has_star:
                ps=lasts+1
                pp=lastp ###
                #while ps<len(s) and pp<len(p) and (s[ps]!=p[pp] and p[pp]!="?"): 
                #    ps+=1 ###won't work for the "**" case
                lasts=ps
            else: return False
        while pp<len(p) and p[pp]=="*": pp+=1 ###
        return pp==len(p)
            
a=Solution()
print a.isMatch("aab","*a*b") #True
print a.isMatch("ab","?*") #True
print a.isMatch("aa","*") #True
print a.isMatch("ho","**ho") #True

#224. Basic Calculator (*)
class Solution(object):
    def calculate(self, s):
        res=0
        stack=[]
        num,sign=0,1
        for i,c in enumerate(s):
            if c in "0123456789":
                num=num*10+int(c)
            #if i==len(s)-1:
            #    res+=num*sign
            #    break
            if c=="+":
                res+=num*sign
                num,sign=0,1
            if c=="-":
                res+=num*sign
                num,sign=0,-1
            if c=="(":
                stack.append(res)
                stack.append(sign)
                # no need for num=0, as it must be set so before ( by + or -
                num,sign=0,1
                res=0
            if c==")":
                res+=num*sign
                #prev_sign=stack.pop()
                #prev_num=stack.pop()
                #cur=prev_sign*res
                #cur+=prev_num
                #res=cur
                res*=stack.pop() # same as above, better writing
                res+=stack.pop()
                num=0 ### only thing missing, no matter what sign is
                      # next c if exist must be +/1, will do res+=num*sign
        if num: res+=sign*num  # same as above, better writing
        return res
            
#a=Solution()
#print a.calculate("1 + 1")
#print a.calculate("68 + 2")
#print a.calculate("-(1+(4-5+2)+3)-(6+8)") #-19
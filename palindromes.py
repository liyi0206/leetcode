# totally 10 palindrome questions
#5	Longest Palindromic Substring (*) - string
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==0: return 0
        maxLen=1
        start=0
        for i in xrange(len(s)): #o(n)
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]

#9	Palindrome Number - easy, array
#125	Valid Palindrome - easy, string & 2P

#131	Palindrome Partitioning - return all partitions. bt
#132	Palindrome Partitioning II (*) - return minCut. DP
class Solution(object):
    def minCut(self, s):
        n=len(s)
        dp=[[False]*n for i in range(n)] #isPalin
        res=[-1]*(n+1) #minCut
        for i in range(n): dp[i][i]=True
        for i in range(n-1,-1,-1):
            res[i]=res[i+1]+1
            for j in range(i+1,n):
                if s[i]==s[j] and (j==i+1 or dp[i+1][j-1]==True):
                    dp[i][j]=True
                    if j==n-1: res[i]=0
                    res[i]=min(res[i],res[j+1]+1)
        return res[0]
        
#214	Shortest Palindrome (*) - google, KMP
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        A=s+"*"+s[::-1]
        cont=[0]
        for i in range(1,len(A)):
            index=cont[i-1]
            while(index>0 and A[index]!=A[i]):
                index=cont[index-1]
            cont.append(index+(1 if A[index]==A[i] else 0))
        return s[cont[-1]:][::-1]+s

#234	Palindrome Linked List - linked list & 2P
# O(n) time and O(1) space
# reverse the second half *
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def isPalindrome(self, head):
        if not head: return None
        
        # find the mid node
        p1,p2=head,head
        while p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
        #print p1.val,p2.val
            
        # reverse the second half
        prev=None
        cur=p1.next #head of the second half
        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        p1.next=prev

        #pp=head
        #while pp:
        #    print pp.val,
        #    pp=pp.next
        
        # compare the first and second half nodes
        p1,p2=head,prev
        while p2: # while node and head:
            if p2.val!= p1.val: return False
            p2 = p2.next
            p1 = p1.next
        return True

root=ListNode(1)
cur=root
for i in range(2,9): #try odd and even numbers
    cur.next=ListNode(i)
    cur=cur.next
a=Solution()
print a.isPalindrome(root)

#266	Palindrome Permutation - easy, google, hash table
#267	Palindrome Permutation II - bt

#336	Palindrome Pairs (*) - google, hash table or trie, o(n*k^2)
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if len(words)<2: return []
        mp={}
        for i,word in enumerate(words): mp[word]=i #words are distinct, o(n)
        
        res=set()
        for i,word in enumerate(words): #o(n*k^2)
            for j in range(len(word)+1): #remember to consider k+1
                str1=word[:j]
                str2=word[j:]
                if self.isPalindrome(str1): # could be str2+str1+rv2
                    rv2=str2[::-1]
                    if rv2 in mp and mp[rv2]!=i: res.add((mp[rv2],i))
                    # mp[rv2]!=i when word is symmetric itself, and there is 
                    # no more such word to concat
                if self.isPalindrome(str2): # could be str1+str2+rv1
                    rv1=str1[::-1]
                    if rv1 in mp and mp[rv1]!=i: res.add((i,mp[rv1]))
        return list(res)
        
    def isPalindrome(self,word):
        n=len(word)
        for i in range(n/2):
            if word[i]!=word[n-i-1]: return False
        return True
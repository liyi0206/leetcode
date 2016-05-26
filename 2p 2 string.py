### 2p - slow and fast
#3. Longest Substring Without Repeating Characters (*)
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        p1,p2=0,0
        res=0
        visited=set()
        while p2<len(s): 
            if s[p2] in visited: 
                res=max(res,p2-p1)
                while s[p2] in visited:
                    visited.remove(s[p1])
                    p1+=1
            visited.add(s[p2])
            p2+=1
        res=max(res,p2-p1)
        return res
        
#a=Solution()
#print a.lengthOfLongestSubstring("abcabcbb")
#print a.lengthOfLongestSubstring("")

#30. Substring with Concatenation of All Words
class SolutionNoDup(object):
    def findSubstring(self,s,words): # words could have dups
        st=set(words)
        l,n=len(words[0]),len(words)
        res=[]
        for start in range(l):
            p1,p2,tmp=start,start,set()
            while p2<len(s):
                if s[p2:p2+l] not in tmp and s[p2:p2+l] in st:
                    tmp.add(s[p2:p2+l])
                    p2+=l
                    if len(tmp)==n: 
                        res.append(p1)
                        tmp.remove(s[p1:p1+l])
                        p1+=l
                elif s[p2:p2+l] in tmp:
                    while s[p2:p2+l] in tmp:
                        tmp.remove(s[p1:p1+l])
                        p1+=l
                    tmp.add(s[p2:p2+l])
                    p2+=l
                else:
                    p1,p2,tmp=p2+l,p2+l,set()
        return res
        
a=SolutionNoDup()
print a.findSubstring("barfoothefoobarman",["foo","bar"])
print a.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])
print a.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])

#76. Minimum Window Substring (**)
# for p2, if in mp update mp, if mp==0 update counter, if counter==0 move p1
# for p1, if in mp update up, if mp>0 update counter, if counter>0 stop and update res
# at the end of each while loop, move pointers
class Solution(object):
    def minWindow(self,s,t):
        mp={}
        for c in t:
            if c not in mp: mp[c]=1
            else: mp[c]+=1
            
        res=""
        counter=len(mp)
        p1,p2=0,0
        while p2<len(s):
            if s[p2] in mp:
                mp[s[p2]]-=1
                if mp[s[p2]]==0: counter-=1
                if counter==0:
                    while counter==0:
                        if s[p1] in mp:
                            mp[s[p1]]+=1
                            if mp[s[p1]]>0: counter+=1
                        p1+=1
                    if res=="" or p2-(p1-1)+1<len(res):
                        res=s[p1-1:p2+1]
            p2+=1
        return res
            
#a=Solution()
#print a.minWindow("ADOBECODEBANC","ABC") #"BANC"
#print a.minWindow("a","aa") #""

#159 Longest Substring with At Most Two Distinct Characters (locked)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp={}
        res=0
        p1,p2=0,0
        while p2<len(s):
            #print p1,p2,mp
            if s[p2] not in mp: mp[s[p2]]=1
            else: mp[s[p2]]+=1
            if len(mp)==3:
                res=max(res,p2-p1)
                while len(mp)>2:
                    #print "inner",p1,p2,mp
                    mp[s[p1]]-=1
                    if mp[s[p1]]==0: mp.pop(s[p1])
                    p1+=1
            p2+=1
        res=max(res,p2-p1)
        return res
        
#a=Solution()
#print a.lengthOfLongestSubstringTwoDistinct('eceba') #3
#print a.lengthOfLongestSubstringTwoDistinct("abcabcabc") #2
#print a.lengthOfLongestSubstringTwoDistinct("a") #1

#340 Longest Substring with At Most K Distinct Characters (locked)
# same as #3, different with #76, update res before moving p1
# same as #3, different with #76, update res at last too
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mp={}
        res=0
        p1,p2=0,0
        while p2<len(s):
            if s[p2] not in mp: mp[s[p2]]=1
            else: mp[s[p2]]+=1
            if len(mp)==k+1:
                res=max(res,p2-p1)
                while len(mp)>k:
                    mp[s[p1]]-=1
                    if mp[s[p1]]==0: mp.pop(s[p1])
                    p1+=1
            p2+=1
        res=max(res,p2-p1)
        return res

#209. Minimum Size Subarray Sum
class Solution(object):
    def minSubArrayLen(self, s, nums):
        p1,p2=0,0
        res=0
        while p2<len(nums):
            if sum(nums[p1:p2+1])>=s:
                while sum(nums[p1:p2+1])>=s: p1+=1
                if res==0 or res>p2-(p1-1)+1: res=p2-(p1-1)+1
            else: p2+=1
        return res
        
#a=Solution()
#print a.minSubArrayLen(7,[2,3,1,2,4,3]) #2
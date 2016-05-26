# 139 Word Break
# 140 Word Break II
class Solution(object):
    def wordBreak(self,s,worddict):
        dp=[1]+[0]*len(s)
        s=" "+s
        for i in range(len(s)):
            if dp[i]==1:
                for word in worddict:
                    if i+1+len(word)<=len(s) and word==s[i+1:i+1+len(word)]:
                        if i+len(word)==len(s)-1: return True
                        dp[i+len(word)]=1
        #print dp
        return dp[-1]==1
                    
#a=Solution()
#print a.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])

class Solution2(object):
    def wordBreak2(self,s,worddict):
        dp=[[] for i in range(len(s)+1)]
        s=" "+s
        for i in range(len(s)):
            if i==0 or dp[i]:
                for word in worddict:
                    if i+1+len(word)<=len(s) and word==s[i+1:i+1+len(word)]:
                        dp[i+len(word)].append(i)
        #print dp
        self.dp=dp
        self.s=s
        self.res=[]
        if len(dp[-1])>0:
            self.bt(len(s)-1,[])
        return self.res
        
    def bt(self,idx,path):
        if idx==0:
            self.res.append(path)
            return
        for elem in self.dp[idx]:
            self.bt(elem,[self.s[elem+1:idx+1]]+path)
        
        
a=Solution2()
print a.wordBreak2("catsanddog",["cat", "cats", "and", "sand", "dog"])



#126 Word Ladder II
#127 Word Ladder

#290 Word Pattern
#291 Word Pattern II

#79  Word Search
#212 Word Search II

#shortest word distances 1-3

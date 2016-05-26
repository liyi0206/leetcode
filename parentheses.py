#20 Valid Parentheses - stack
class Solution(object):
    def isValid(self,s):
        stack=[]
        mp={"(":")","{":"}","[":"]"}
        for c in s:
            if c in "({[": 
                stack.append(c)
            if c in ")}]": 
                if not stack: return False
                tmp=stack.pop()
                if c!=mp[tmp]: return False
        return stack==[]

#a=Solution()
#print a.isValid("()[]{}")
#print a.isValid("([)]")

#22 generate parentheses - dfs
class Solution(object):
    def generateParenthesis(self,n): #TLE
        if n<1: return None
        self.res=[]
        self.bt(n-1,"()")
        return self.res
        
    def bt(self,x,tmp):
        if x==0:
            if tmp not in self.res:
                self.res.append(tmp)
            return
        for i in range(len(tmp)+1):
            self.bt(x-1,tmp[:i]+"()"+tmp[i:])
            
class Solution22(object): #smart!!
    def generateParenthesis(self,n):
        if n<1: return None
        self.res=[]
        self.bt(n,n,"")
        return self.res
        
    def bt(self,left,right,tmp):
        if left==0 and right==0:
            self.res.append(tmp)
            return
        if left>0: 
            self.bt(left-1,right,tmp+"(")
        if left<right:
            self.bt(left,right-1,tmp+")")

#a=Solution22()
#print a.generateParenthesis(3) #"((()))", "(()())", "(())()", "()(())", "()()()"

#32 Longest Valid Parentheses - DP Hard! - stack Harder!
class Solution(object): #DP
    def longestValidParentheses(self, s):
        if not s: return 0
        dp=[0]*len(s)
        for i in range(len(s)-2,-1,-1):
            if s[i]=="(":
                j=i+1+dp[i+1]
                if j<len(s) and s[j]==")":
                    dp[i]=dp[i+1]+2
                    if j+1<len(s): dp[i]+=dp[j+1]
        return max(dp)

class Solution32(object): #STACK
    def longestValidParentheses(self, s):
        res,last,stack = 0,-1,[]
        for i in range(len(s)):
            if s[i]=='(': stack.append(i)
            elif len(stack)==0: last = i
            elif len(stack)==1:
                res = max(res,i-last)
                stack.pop()
            else:
                res = max(res,i-stack[-2])
                stack.pop()
        return res

a=Solution()
print a.longestValidParentheses("(()") #2
print a.longestValidParentheses(")()())")#4
print a.longestValidParentheses("()(()") #2

#241 Different Ways to Add Parentheses - divide and conquer
# solution1 problems - 
#(((2*3)-4)*5) = 10
#((2*3)-(4*5)) = -14
#((2*(3-4))*5) = -10
#(2*((3-4)*5)) = -10
#no more ((2*3)-(4*5)) = -14!!
#(2*(3-(4*5))) = -34
# so need to append expression than eval value!!

# problem2, several digit nums
# need to use #import re
#input = re.split(r'(\D)', input)

class Solution(object): 
    def diffWaysToCompute(self,input):
        self.res=[]
        operands=[]
        operators=[]
        for i,c in enumerate(input):
            if i%2==0: operands.append(c)
            else: operators.append(c)
        self.bt(operators,operands)
        return sorted([int(a) for a in self.res])
        
    def bt(self,operators,operands):
        if not operators:
            self.res.append(operands[0])
            return
        for i in range(len(operators)):
            self.bt(operators[:i]+operators[i+1:], operands[:i]+\
                    [str(eval(operands[i]+operators[i]+operands[i+1]))]+\
                     operands[i+2:])
                     
class Solution241(object):
    def diffWaysToCompute(self,input):
        self.res=[]
        import re
        input = re.split(r'(\D)', input)
        ops,nums=[],[]
        for i,c in enumerate(input):
            if i%2==0: nums.append(c)
            else: ops.append(c)
        self.bt(ops,nums)
        return sorted([eval(a) for a in self.res])
        
    def bt(self,ops,nums):
        if not ops:
            #print nums[0]
            if nums[0] not in self.res:
                self.res.append(nums[0])
            return
        for i in range(len(ops)):
            self.bt(ops[:i]+ops[i+1:], \
                    nums[:i]+["("+nums[i]+ops[i]+nums[i+1]+")"]+nums[i+2:])
        
a=Solution241()
#print a.diffWaysToCompute("2-1-1") #[0,2]
#print a.diffWaysToCompute("2*3-4*5") #[-34, -14, -10, -10, 10]

#301. Remove Invalid Parentheses - dfs HARD
class Solution(object):
    def removeInvalidParentheses(self,s): #o(n!)
        self.visited=set([s])
        self.res=[]
        self.bt(s)
        return self.res
        
    def bt(self,s):
        tmp=self.calc(s)
        if tmp==0: 
            self.res.append(s) ###
            return
        for i in range(len(s)):
            if s[i] in "()":
                ns=s[:i]+s[i+1:]
                if ns not in self.visited and self.calc(ns)<tmp:
                    self.visited.add(ns)
                    self.bt(ns)
    
    def calc(self,s):
        a,b=0,0
        stack=[]
        for c in s:
            if c=="(": stack.append(c)
            elif c==")": 
                if not stack: b+=1
                else: stack.pop()
        a+=len(stack)
        return a+b
                    
a=Solution()
#a.calc("()())()") #1
#print a.removeInvalidParentheses("()())()")
#print a.removeInvalidParentheses("(a)())()")
#print a.removeInvalidParentheses(")(")
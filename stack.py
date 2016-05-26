#71. Simplify Path (*)
# remember to add if stack when stack.pop()
class Solution(object):
    def simplifyPath(self,path):
        elems=path.split('/')
        stack=[]
        for elem in elems:
            if elem not in ('..','.',''):
                stack.append(elem)
            elif elem=='..':
                if stack: stack.pop()
        return '/'+'/'.join(stack)
        
a=Solution()
#print a.simplifyPath("/home/")
#print a.simplifyPath("/a/./b/../../c/")

#150. Evaluate Reverse Polish Notation ()
# python problem - / negative takes floor not ceiling
class Solution(object):
    def evalRPN(self,tokens):
        stack=[]
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else: 
                num2=stack.pop()
                num1=stack.pop()
                num=eval(num1+token+num2)
                if token=="/":
                    sign=-1 if (int(num1)<0)^(int(num2)<0) else 1
                    num=abs(int(num1))/abs(int(num2))*sign
                stack.append(str(num))
        return int(stack[0])
        
a=Solution()
#print a.evalRPN(["2", "1", "+", "3", "*"]) #9
#print a.evalRPN(["4", "13","5", "/", "+"]) #6
#print a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) #22

#224. Basic Calculator (**)
#227. Basic Calculator II (*)
class Solution(object):
    def calculate(self,s):
        pass
        
a=Solution()
print a.calculate("3+2*2")
print a.calculate(" 3/2 ")
print a.calculate(" 3+5 / 2 ")

#84. Largest Rectangle in Histogram (*)
# width = i or i-1-stack[-1], which is from popped tmp to cur, or from beginning to cur
# the if/else under for loop could be removed
class Solution(object):
    def largestRectangleArea(self,heights):
        heights+=[0]
        stack=[]
        res=0
        for i,h in enumerate(heights):
            #if not stack or h>=heights[stack[-1]]:
            #    stack.append(i)
            #else: 
                while stack and heights[stack[-1]]>h:
                    tmp=stack.pop()
                    if stack: width=i-1-stack[-1]
                    else: width=i
                    area=width*heights[tmp]
                    res=max(res,area)
                stack.append(i)
        return res
        
a=Solution()
print a.largestRectangleArea([2,1,5,6,2,3]) #10
print a.largestRectangleArea([]) #0
print a.largestRectangleArea([1]) #1

#85. Maximal Rectangle (*)
#239. Sliding Window Maximum (*)
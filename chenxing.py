# -*- coding: utf-8 -*-
"""
第一轮是中国小哥，问题是 给定一个9位的键盘，
1 2 3
4 5 6
7 8 9
只有中间没有其他键的两个键才能相连，比如1可以连 2 4 5 6 8 但不能连 3 7 9.
但是如果中间键被使用了，那就可以连，比如5已经被使用了，那1就可以连9
每个键只能用一次，给定一个长度L，求问有多少unique path with length L

中国小哥人很好，循循善诱，见我卡住了就说先写brute force吧，然后再提示说用回溯法
"""

class Solution(object):
    def keyboard(self,l):
        self.mp =  {1:{2:3,5:9,4:7},
                    2:{5:8},
                    3:{2:1,5:7,6:9},
                    4:{5:6},
                    5:{},
                    6:{5:4},
                    7:{4:1,5:3,8:9},
                    8:{5:2},
                    9:{5:1,6:3,8:7}}
        self.visited=[None]+[0]*9
        self.res=0
        for i in range(1,10): self.bt(i,l)
        return self.res
        
    def bt(self,num,l):
        if l==0:
            self.res+=1
            return
        self.visited[num]=1
        disables=[]
        for blocker in self.mp[num]:
            if self.visited[blocker]==1:
                disables.append(self.mp[num][blocker])
        for j in range(1,10):
            if j!=num and j not in disables and self.visited[j]==0: 
                self.bt(j,l-1)
        self.visited[num]=0

a=Solution()
print a.keyboard(4)



class Wrong(object):
    def keyboard(self,l):
        self.mp  = {1:[2,4,5,6,8],
                    2:[1,3,4,5,6,7,9],
                    3:[2,4,5,6,8],
                    4:[1,2,3,5,7,8,9],
                    5:[1,2,3,4,6,7,8,9],
                    6:[1,2,3,5,7,8,9],
                    7:[2,4,5,6,8],
                    8:[1,3,4,5,6,7,9],
                    9:[2,4,5,6,8]}
        self.visited=[None]+[0]*9
        self.res=0
        for i in range(1,10):
            self.bt(i,l)
        return self.res
            
    def bt(self,num,l):
        if l==0: 
            self.res+=1
            return
        self.visited[num]=1
        for elem in self.mp[num]:
            if self.visited[elem]==0:
                self.bt(elem,l-1)
        self.visited[num]=0
        

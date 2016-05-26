# -*- coding: utf-8 -*-
##30. Substring with Concatenation of All Words
##1, do not need flag, check if tmp==[] to see whether count
##2, dup words, need list, not set
##3, range(n-w+1), need +1
#
#class Solution(object):
#    def findSubstring(self,s,words): #TLE
#        n,l,w=len(s),len(words[0]),len(words[0])*len(words)
#        res=[]
#        for i in range(n-w+1):
#            segs=s[i:i+w]
#            tmp=words[:]
#            for k in range(0,w,l):
#                if segs[k:k+l] in tmp:
#                    tmp.remove(segs[k:k+l])
#                else: break
#            if tmp==[]: res.append(i)
#        return res
#
##4, do not need extra tmp=words for remove, vectorize segs and use it for remove       
##5, use for word in words, not for seg in segs, as segs are removing
# 
#    def findSubstring2(self,s,words):
#        n,l,w=len(s),len(words[0]),len(words[0])*len(words)
#        res=[]
#        for i in range(n-w+1):
#            segs=[s[j:j+l] for j in range(i,i+w,l)]
#            for word in words:
#                if word in segs: segs.remove(word)
#                else: break
#            if segs==[]: res.append(i)
#        return res
        
#a=Solution()
#print a.findSubstring2("barfoothefoobarman",["foo", "bar"]) #[0,9]
#print a.findSubstring2("wordgoodgoodgoodbestword",["word","good","best","good"]) #[8]

#149 max points in a line
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#1,consider point2==point1
#2,slope=float(...)
class Solution(object):
    def maxPoints(self, points): #o(n^2)
        res=0
        for i in range(len(points)):
            mp={}
            point1=points[i]
            for j in range(len(points)):
                point2=points[j]
                if point1.x==point2.x and point1.y==point2.y: slope='self'
                elif point2.x==point1.x: slope='inf'
                else: slope=float(point2.y-point1.y)/(point2.x-point1.x)
                
                if slope not in mp: mp[slope]=1
                else: mp[slope]+=1
            non_self=[mp[k] for k in mp if k!='self']
            max_non_self=max(non_self) if non_self else 0 
            res=max(res,max_non_self+mp['self'])
        return res

input=[[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
points=[]
for item in input: points.append(Point(item[0],item[1]))

#x=[a[0] for a in input]
#y=[a[1] for a in input]
#import matplotlib.pyplot as plt
#plt.plot(x,y, 'ro')

#a=Solution()
#print a.maxPoints(points) #expect 22
#print a.maxPoints([])
#print a.maxPoints([Point(1,1)])
#print a.maxPoints([Point(1,1),Point(2,2)])

#274. H-Index

#166. Fraction to Recurring Decimal (**)
#(1) take cares of 0 denominator, negative, abs(), int part first.
#(2) if residual, create map for residual location in result.
#each time r*=10, res+=str(r/d), r%=d
#(3) if meet same residual, find prev loc. res=res[:loc]+”(“+res[loc:]+”)"
#if never meet, return limited res

#128. Longest Consecutive Sequence - make set for all elem, pop elem until empty, find the range from it, remove those elems from set

#II. sum problems
#1. Two Sum
#18. 4Sum
#170. Two Sum III - Data structure design

#III. simple (not even need hash table)
#28. Implement strStr() - naive needle in hay, no need for KPM
#49. Group Anagrams
#169. Majority Element
#187. Repeated DNA Sequences
#202. Happy Number
#204. Count Primes - Sieve of Eratosthenes
#205. Isomorphic Strings
#217. Contains Duplicate
#219. Contains Duplicate II
#242. Valid Anagram
#(1) return sorted(s)==sorted(t) - simple, but o(nlogn)
#(2) hash table - o(n)
#290. Word Pattern
#299. Bulls and Cows
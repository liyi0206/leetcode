class Solution(object):
    def merge(self,intervals):
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][1]: res.append(intervals[i])
            else: res[-1][1]=max(intervals[i][1],res[-1][1])
        return res

#a=Solution()
#print a.merge([[1,3],[2,6],[8,10],[15,18]]) #[1,6],[8,10],[15,18]

class Solution(object):
    def insert(self,intervals,newInterval):
        if not intervals: return [newInterval]
        i=0
        while i<len(intervals) and intervals[i][1]<newInterval[0]: i+=1
        idx=i
        mergeInterval=[newInterval[0],newInterval[1]]
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            mergeInterval[0]=min(intervals[i][0],mergeInterval[0])
            mergeInterval[1]=max(intervals[i][1],mergeInterval[1])
            i+=1
        return intervals[:idx]+[mergeInterval]+intervals[i:]
        
a=Solution()
print a.insert([[1,3],[6,9]],[2,5]) #[1,5],[6,9]
print a.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,9]) #[1,2],[3,10],[12,16]
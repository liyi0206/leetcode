class Solution(object):
    def twoSum(self,nums,target):
        mp={}
        for i,num in enumerate(nums):
            if target-num in mp:
                return [mp[target-num],i]
            mp[num]=i
                
#a=Solution()
#print a.twoSum([2,7,11,15], 9)

class Solution2(object):
    def threeSum(self,nums):
        nums.sort()
        res=[]
        for i,num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]: continue ### i>0
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[j]+nums[k]+num==0:
                    #if [num,nums[j],nums[k]] not in res:
                    res.append([num,nums[j],nums[k]])
                    j,k=j+1,k-1
                    while j<k and nums[j]==nums[j-1]: j+=1
                    while j<k and nums[k]==nums[k+1]: k-=1
                elif nums[j]+nums[k]+num>0: k-=1
                else: j+=1
        return res 
        
#a=Solution2()
#print a.threeSum([-1,0,1,2,-1,-4])
#print a.threeSum([0,0,0])

class Solution22(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        diff,res=100000000,-1
        for i,num in enumerate(nums):
            j,k=i+1,len(nums)-1
            while j<k:
                tmp=nums[j]+nums[k]+num-target
                if abs(tmp)<diff: 
                    res=nums[j]+nums[k]+num
                    diff=abs(tmp)
                if tmp==0: return target
                elif tmp>0: k-=1
                else: j+=1
        return res
        
#a=Solution22()
#print a.threeSumClosest([-1,2,1,-4],1)
#print a.threeSumClosest([1,1,1,0],-100)

class Solution3(object):
    def fourSum(self,nums,target):
        nums.sort()
        mp={}
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                tmp=nums[i]+nums[j]
                if tmp not in mp: mp[tmp]=[(i,j)]
                else: mp[tmp].append((i,j))
        for k in range(len(nums)):
            for l in range(k+1,len(nums)-2):
                tmp= target-nums[k]-nums[l]
                if tmp in mp:
                    for elem in mp[tmp]:
                       if l<elem[0]: res.add((nums[k],nums[l],nums[elem[0]],nums[elem[1]]))
        return [list(a) for a in res]
                    
a=Solution3()
print a.fourSum([1,0,-1,0,-2,2],0)

# o(n^2) 
# might have dups, use res set, then convert
# if l<elem[0] prunes some dup branches
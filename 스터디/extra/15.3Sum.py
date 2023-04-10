# https://leetcode.com/problems/3sum/description/

# 4문제 남기고 시간초과
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    val=(nums[i]+nums[j])*(-1)
                    if val in nums and nums.index(val) not in (i,j):
                        cand=sorted([nums[i],nums[j],val])
                        if cand not in answer:
                            answer.append(cand)
        return answer
    
# 통과
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort() 
        l=[]
        for i in range(len(nums)):  
            if i>0 and nums[i-1]==nums[i]:  
                continue 
            j=i+1 
            k=len(nums)-1 
            while j<k: 
                s=nums[i]+nums[j]+nums[k] 
                if s>0: 
                    k-=1 
                elif s<0: 
                    j+=1
                else:
                    l.append([nums[i],nums[j],nums[k]]) 
                    j+=1 
                    while nums[j-1]==nums[j] and j<k:
                        j+=1   
        return l
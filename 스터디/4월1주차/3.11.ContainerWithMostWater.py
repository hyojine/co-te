# https://leetcode.com/problems/container-with-most-water/description/

# 이중 for문으로 TimeLimitExceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        water=0
        for i in range(len(height)):
            for j in range(len(height)):
                if i+j>len(height)-1:
                    break
                if j*min(height[i],height[i+j])>water:
                    water=j*min(height[i],height[i+j])
        return water
       
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        answer=0
        while start<=end:
            area=min(height[end],height[start])*(end-start)
            answer=max(answer,area)
            if height[end]>height[start]:
                start+=1
            else:
                end-=1
        return answer
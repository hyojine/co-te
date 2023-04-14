# https://leetcode.com/problems/container-with-most-water/description/

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
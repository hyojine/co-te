# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

def findMedianSortedArrays(nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            return (nums1[len(nums1)//2-1]+nums1[len(nums1)//2])/2
        else:
            return nums1[len(nums1)//2]
        

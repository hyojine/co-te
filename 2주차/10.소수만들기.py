from itertools import combinations

def solution(nums):
    count = 0
    for a, b, c in combinations(nums, 3):
        if len([i for i in range(1, (a+b+c+1)) if (a+b+c) % i == 0]) == 2:
            count += 1
    return count

def solution(nums):
    count = 0
    for a, b, c in combinations(nums, 3):
        if len([(i, (a+b+c)//i) for i in range(1, int((a+b+c)**0.5)+1) if (a+b+c) % i == 0]) == 1:
            count += 1
    return count

def solution3(nums):
    count = 0
    nums=list(set(nums))
    for idx, i in enumerate(nums[:-2]):
        for j in nums[idx+1:-1]:
            for k in nums[nums.index(j)+1:]:
                total = i+j+k
                if len([(x, total//x) for x in range(1, int(total**0.5)+1) if (total) % x == 0]) == 1:
                    count += 1
    return count
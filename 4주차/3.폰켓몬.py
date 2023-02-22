def solution(nums):
    if len(set(nums))>len(nums)/2:
        return len(nums)/2
    else:
        return len(set(nums))
# 테스트 15 〉	통과 (0.07ms, 10.3MB)
# 테스트 16 〉	통과 (1.01ms, 11.1MB)
# 테스트 17 〉	통과 (1.03ms, 10.4MB)
# 테스트 18 〉	통과 (0.69ms, 10.5MB)
# 테스트 19 〉	통과 (0.78ms, 10.3MB)
# 테스트 20 〉	통과 (0.76ms, 10.3MB)


def solution(nums):
    len_nums=len(set(nums))
    ans=len(nums)/2
    if len_nums>ans:
        return ans
    else:
        return len_nums
# 테스트 15 〉	통과 (0.03ms, 10MB)
# 테스트 16 〉	통과 (0.74ms, 11MB)
# 테스트 17 〉	통과 (0.53ms, 10.6MB)
# 테스트 18 〉	통과 (0.35ms, 10.5MB)
# 테스트 19 〉	통과 (0.24ms, 10.2MB)
# 테스트 20 〉	통과 (0.18ms, 10.4MB)

def solution(nums):
    return min(len(nums)/2,len(set(nums)))

# 테스트 15 〉	통과 (0.05ms, 10.3MB)
# 테스트 16 〉	통과 (0.74ms, 11.1MB)
# 테스트 17 〉	통과 (0.41ms, 10.5MB)
# 테스트 18 〉	통과 (0.39ms, 10.4MB)
# 테스트 19 〉	통과 (0.24ms, 10.4MB)
# 테스트 20 〉	통과 (0.20ms, 10.3MB)
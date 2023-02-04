def solution(arr, divisor):
    if not [x for x in arr if x%divisor==0]:
        return [-1]
    return sorted([x for x in arr if x%divisor==0])

def solution(arr, divisor):
    return sorted([x for x in arr if x%divisor==0]) or [-1]
    # return sorted([x for x in arr if x%divisor==0]) if len(arr) != 0 else [-1];

# def solution(arr, divisor):
#     for element in arr:
#         print(arr.index(element),element)
#         if element%divisor!=0:
#             arr.remove(element)
#     if not arr:
#         arr.append(-1)
#     return sorted(arr)
# solution([5, 9, 7, 10], 5)
# 혹시 7을 건너뛰나..? 진짜야.. 10 인덱스가 2로 나옴.
# 그럼 7 인덱스가 자동으로 1이 된거아냐..
# 이럴거면 인덱스로 하는거랑 뭐가 다르지


print(solution2(4,[4,4,4,4,4]))
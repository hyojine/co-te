def solution(arr, divisor):
    if not [x for x in arr if x%divisor==0]:
        return [-1]
    return sorted([x for x in arr if x%divisor==0])
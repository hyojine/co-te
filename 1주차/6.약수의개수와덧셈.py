def solution(left, right):
    total = sum(list(range(left,right+1)))
    odd = 0
    even = 0
    for i in list(range(left,right+1)):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count += 1
        if count%2 != 0:
            odd -= i
        else:
            even += i
    return even+odd
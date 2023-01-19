def solution(a, b):
    if a>b:
        a,b=b,a
    if a<b:
        sum_list=[a]
        while a<b:
            a=a+1
            sum_list.append(a)
        return sum(sum_list)
    elif a==b:
        return a

# 2번째
def solution(a, b):
    big = max([a,b])
    small = min([a,b])
    total = 0
    if small == big:
        return small
    while small<big:
        total+=small
        small+=1
    return total+big
    
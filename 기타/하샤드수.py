def solution(x):
    total=0
    y=x
    while y>10:
        total+=y%10
        y=y//10
    total+=y
    if x%total==0:
        return True
    else:
        return False

# 수정
def solution(x):
    total=0
    y=x
    while y>10:
        total+=y%10
        y=y//10
    total+=y
    return x%total==0

# 스트링으로
def solution(x):
    x=str(x)
    total=0
    for i in x:
        total+=int(i)
    return int(x)%total==0
    
# 리스트 축약식으로
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0
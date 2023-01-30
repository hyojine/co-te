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
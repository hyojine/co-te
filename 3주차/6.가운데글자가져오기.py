def solution(s):
    answer=[]
    if len(s)%2==0:
        index_x=len(s)//2-1
        index_y=len(s)//2
        index=s[index_x]+s[index_y]
    elif len(s)%2!=0:
        index=len(s)//2
        index=s[index]
    return index
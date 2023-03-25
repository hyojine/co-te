# https://www.acmicpc.net/submit/1920/58113808
import sys

n=int(input())
nlist=set(map(int,sys.stdin.readline().split()))
m=int(input())
mlist=list(map(int,sys.stdin.readline().split()))

# for mm in mlist:
#     if mm in nlist:
#         print(1)  
#     else:
#         print(0)
for mm in mlist:
    print(1) if mm in nlist else print(0)


# 이분탐색        
import sys

n=int(input())
nlist=sorted(map(int,sys.stdin.readline().split()))
m=int(input())
mlist=list(map(int,sys.stdin.readline().split()))

for mm in mlist:
    start=0
    end=n-1
    while start<=end:
        if mm==nlist[(start+end)//2]:
            print(1)
            break
        elif mm < nlist[(start+end)//2]:
            end=(start+end)//2-1
        elif mm > nlist[(start+end)//2]:
            start=(start+end)//2+1
    if start>end:
        print(0)

# 이분탐색 함수형
import sys

def solution(target,start,end):
    while start<=end:
        mid=(start+end)//2
        if target==nlist[mid]:
            return 1
        elif target < nlist[mid]:
            end=mid-1
        elif target > nlist[mid]:
            start=mid+1
    if start>end:
        return 0

n=int(input())
nlist=sorted(map(int,sys.stdin.readline().split()))
m=int(input())
mlist=list(map(int,sys.stdin.readline().split()))

for mm in mlist:
    start=0
    end=n-1
    print(solution(mm,start,end))

# 재귀
import sys

def solution(target,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if target==nlist[mid]:
        return 1
    elif target < nlist[mid]:
        end=mid-1
    elif target > nlist[mid]:
        start=mid+1
    return solution(target,start,end)

n=int(input())
nlist=sorted(map(int,sys.stdin.readline().split()))
m=int(input())
mlist=list(map(int,sys.stdin.readline().split()))

for mm in mlist:
    start=0
    end=n-1
    print(solution(mm,start,end))
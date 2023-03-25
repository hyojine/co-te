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

start=0
end=n-1
for mm in mlist:
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
import sys
from heapq import heappop, heappush

N=int(sys.stdin.readline())
# N=int(input())
heap=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x==0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap,x)
    
from heapq import heappop, heappush

N=int(input())
heap=[]

for _ in range(N):
    x=int(input())
    if x==0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    elif x>0:
        heappush(heap,x)
    
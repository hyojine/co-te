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
        
    
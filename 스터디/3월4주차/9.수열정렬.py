# https://www.acmicpc.net/status?user_id=touroz&problem_id=1015&from_mine=1

# B[P[i]] = A[i] 길이가 N
# 수열 P: 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열
# 비내림차순: 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우
# 만약 그러한 수열이 여러 개라면 사전순으로 앞서는 것을 출력한다
# N : 배열 A의 크기 #N은 50보다 작거나 같은 자연수
# 배열 A의 원소 : 1000보다 작거나 같은 자연수

n=int(input())
network=list(map(int,input().split()))
idx=sorted(network)

ans=[]

for i,net in enumerate(network):
    ans.append(idx.index(net))
    idx[idx.index(net)]=0

print(*ans)

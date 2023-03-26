# https://www.acmicpc.net/problem/2606

computer = int(input())
pairs = int(input())
graph = [[] for _ in range(computer+1)]
visited = [0] * (computer + 1)
for _ in range(pairs):
    from_p, to_p = map(int, input().split())
    graph[from_p].append(to_p)
    graph[to_p].append(from_p)
    
visited[1] = 1 # 1번 컴퓨터 감염
stack = [1]
v=1
while stack:
    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = 1
            stack.append(v)
            v = w
            break
    else:
        v = stack.pop()
            
print(sum(visited)-1) 
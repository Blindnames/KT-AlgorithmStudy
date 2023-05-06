INF = int(1e9) 

n, m = map(int, input().split())

# 자기 자신에서 자기 자신은 0
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
           
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = n
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF and graph[j][i] == INF:
            count-=1
            break
        
print(count)
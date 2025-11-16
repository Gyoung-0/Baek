import heapq
def solution(N, road, K):
    # 양방향으로 통행할 수 있는 도로
    graph = [[] for _ in range(N+1)]
    print(graph)
    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    dist = [float('inf')] * (N+1)
    start = []
    dist[1] = 0
    heapq.heappush(start, (0, 1)) # cost, 시작위치
    
    while start:
        current_cost, current_node= heapq.heappop(start)
        if current_cost > dist[current_node]:
            continue
        for next_node, next_cost in graph[current_node]:
            new_cost = next_cost + current_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(start, (new_cost,next_node))
    answer = 0
    for i in dist:
        if i <= K:
            answer += 1
    return answer
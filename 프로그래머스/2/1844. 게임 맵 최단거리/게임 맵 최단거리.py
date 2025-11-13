from collections import deque
def solution(maps):
    # 최단거리 BFS
    n, m = len(maps), len(maps[0]) # 행렬
    # 방문한 곳은 다시 가지 않게
    visited = [[False] * m for _ in range(n)]
    
    # 이동방향
    directions = (1, 0), (-1, 0), (0, 1), (0, -1)
    
    q = deque()
    q.append((0,0,1)) # 출발 행, 출발 열, 이동 거리
    visited[0][0] = True # 처음 출발 위치는 방문했음
    
    while q:
        current_n, current_m, dist = q.popleft()
        if current_n == n-1 and current_m == m-1:
            return dist
        for dn, dm in directions:
            next_n, next_m = current_n + dn, current_m + dm
            if not (0 <= next_n < n and 0 <= next_m < m):
                continue
            if visited[next_n][next_m] == True:
                continue
            if maps[next_n][next_m] == 0:
                continue
            current_dist = dist
            
            q.append((next_n, next_m, dist+1))
            visited[next_n][next_m] = True
        print(dist)
    return -1
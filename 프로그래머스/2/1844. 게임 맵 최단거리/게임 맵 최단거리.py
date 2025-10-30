from collections import deque
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)] 
    
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True
    dist = 1
    directions = (-1, 0), (1, 0), (0, -1), (0, 1)
    
    while q:
        cn, cm, dist = q.popleft()
        if cn == n-1 and cm == m-1:
            return dist
        for dx, dy in directions:
            cdist = dist    
            nx, ny = dx+cn, dy+cm
            
            if not (0<=nx<n and 0<=ny<m):
                continue
            if visited[nx][ny] == True:
                continue
            if maps[nx][ny] == 0:
                continue
            
            q.append((nx, ny, cdist+1))
            visited[nx][ny] = True
            
            
    return -1
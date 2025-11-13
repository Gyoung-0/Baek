from collections import deque
def solution(maps):
    # target의 위치를 반환하는 함수
    def find_position(maps, target):
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == target:
                    return i, j
    # 최단 거리는 BFS
    
    n, m = len(maps), len(maps[0]) # 행렬
    
    start_n, start_m = find_position(maps, 'S')
    
    # 이동 방향
    directions = (-1, 0), (1, 0), (0, -1), (0, 1)
    
    # 방문한 곳은 재방문 하지 않음
    # 레버가 당겨졌을때 안땡겨졌을때 구분해야함
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    q = deque()
    q.append((start_n, start_m, False, 0)) # 시작 위치 n, m , 레버 유무, 이동 거리
    visited[start_n][start_m][0] = True
    
    while q:
        currnet_n, current_m, lever, dist = q.popleft()
        if lever == 1 and maps[currnet_n][current_m] == 'E':
            return dist
        for dn, dm in directions:
            next_n, next_m = dn+currnet_n, dm+current_m
            if not (0<=next_n<n and 0<=next_m<m):
                continue
            if visited[next_n][next_m][lever]:
                continue
            if maps[next_n][next_m] == 'X':
                continue
            
            if maps[next_n][next_m] == 'L':    
                q.append((next_n, next_m, 1, dist+1))
                visited[next_n][next_m][1] = True
                continue
            q.append((next_n, next_m, lever, dist+1))
            visited[next_n][next_m][lever] = True

    return -1
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    # 1) 시작점 찾기
    start = find_start(maps)
    if start is None:
        return -1
    sr, sc = start

    # 2) visited[r][c][lever] : lever=0(안당김), 1(당김)
    visited = [[[False]*2 for _ in range(m)] for __ in range(n)]
    q = deque()
    q.append((sr, sc, 0, 0))  # (r, c, lever, dist)
    visited[sr][sc][0] = True

    # 3) 상하좌우
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    # 4) BFS
    while q:
        r, c, lever, dist = q.popleft()

        # 레버를 당긴 상태에서만 E 도착을 인정
        if maps[r][c] == 'E' and lever == 1:
            return dist

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # 범위 체크 먼저
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            # 벽 제외
            if maps[nr][nc] == 'X':
                continue

            nlever = lever
            # 레버 발견 시 상태 전환
            if maps[nr][nc] == 'L':
                nlever = 1

            if not visited[nr][nc][nlever]:
                visited[nr][nc][nlever] = True
                q.append((nr, nc, nlever, dist + 1))
    return -1

def find_start(maps):
    for i, row in enumerate(maps):
        for j, cell in enumerate(row):
            if cell == 'S':
                return (i, j)
    return None
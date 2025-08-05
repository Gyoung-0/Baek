from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]

    # 1. 시작 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)

    # 2. 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 3. BFS
    queue = deque([(start[0], start[1], 0)])  # x, y, move

    while queue:
        x, y, move = queue.popleft()

        if board[x][y] == 'G':
            return move

        for dx, dy in directions:
            nx, ny = x, y

            # 벽 또는 장애물 만날 때까지 직진
            while 0 <= nx+dx < n and 0 <= ny+dy < m and board[nx+dx][ny+dy] != 'D':
                nx += dx
                ny += dy

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, move + 1))

    return -1  # 도달 못하면 -1
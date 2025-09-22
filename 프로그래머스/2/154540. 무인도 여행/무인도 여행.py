from collections import deque
def solution(maps):
    answer = []
    # maps에 'X'만 있으면 return -1
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for __ in range(n)]
    directions = (-1, 0), (1, 0), (0, -1), (0, 1)
    q = deque()
    total = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == True:
                continue
            cell = maps[i][j]
            if cell.isdigit():
                num = int(cell)
                if 0 < num < 10:
                    q.append((i,j))
                    total = num
                    visited[i][j] = True
                while q:
                    sn, sm = q.popleft()

                    for x, y in directions:
                        nx, ny = sn+x, sm+y

                        if not(0<= nx <n and 0 <= ny < m):
                            continue
                        if maps[nx][ny] == 'X':
                            continue

                        cell = maps[nx][ny]
                        if visited[nx][ny] == False and cell.isdigit():
                            num = int(cell)
                            if 0 < num < 10:
                                q.append((nx, ny))
                                total += num
                                visited[nx][ny] = True
                answer.append(total)
    if not answer:
        return [-1]
    

    return sorted(answer)
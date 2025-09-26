from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])
    visited = set([x])
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == y:
            return cnt
        for nx in (cur*2, cur*3, cur+n):
            if nx <= y and nx not in visited:
                q.append((nx, cnt+1))
                visited.add(nx)
                
    return -1
        
    
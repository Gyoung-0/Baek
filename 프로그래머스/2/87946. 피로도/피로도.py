from typing import List
def solution(k: int, dungeons: List[List[int]]) -> int:
    # 최대한 많이 -> dfs 
    
    # 일단 해당 던전을 방문 했는지 안했는지 알아야함
    n = len(dungeons)
    visited = [False] * n
    max_dungeons = 0
    # dfs에 뭐가 필요할까 일단 현재 피로도, 현재 돌은 던전 수
    def dfs(fatigue: int, count: int) -> int:
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, count)
        for i in range(n):
            required, cost = dungeons[i]
            
            if not visited[i] and fatigue >= required:
                visited[i] = True
                
                dfs(fatigue-cost, count+1)
                visited[i] = False
    dfs(k, 0)
    return max_dungeons
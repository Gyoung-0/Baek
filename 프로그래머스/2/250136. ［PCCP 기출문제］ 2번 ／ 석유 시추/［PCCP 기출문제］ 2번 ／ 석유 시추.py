from collections import deque
def solution(land):
    answer = 0
    # 석유관이 수직으로 들어가면 0~n열까지 중 수직으로 뚫고 들어가며 ==1과 만나면 이 x,y 좌표에 해당하는 각 방향 ==1 인곳을 다 돌면서 다 더해서 리턴하면 될 거 같은데 -> 효율성 테스트 실패
    # 한번 돌은 땅은 더 안돌게 기록해놓으면 될듯
    n, m = len(land), len(land[0])
    # 1. 모든 땅을 돌면서 기록해두기
    q = deque()
    oils = {}
    directions = (1, 0), (-1, 0), (0, 1), (0, -1)
    current_oil = 2 # 0은 그냥 땅 , 1은 아직 안돌아본 오일이 있는곳
    for i in range(n):
        for j in range(m):
            current_land = land[i][j]
            if current_land == 1:
                q.append((i, j)) 
                land[i][j] = current_oil
                size=1
                
                while q:
                    cn, cm = q.popleft()
                    for dn, dm in directions:
                        dx, dy = cn+dn, cm+dm
                        
                        if (0 <= dx < n and 0 <= dy < m) and land[dx][dy] == 1:
                            land[dx][dy] = current_oil
                            q.append((dx, dy))
                            size += 1
                
                oils[current_oil] = size
                current_oil += 1         
    max_oil = 0
    for col in range(m):
        seen = set()
        total = 0
        for row in range(n):
            oil_id = land[row][col]
            if oil_id > 1 and oil_id not in seen:
                seen.add(oil_id)
                total += oils[oil_id]
        max_oil = max(max_oil, total)
            
    
    
        
    
    return max_oil
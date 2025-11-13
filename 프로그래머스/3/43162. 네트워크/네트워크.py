def solution(n, computers):
    answer = 0
    # 방문했는지, 1번에서 연결된거 다 가고 방문한거 표시, 해당 인덱스 배열은 스킵
    visited = [False] * n
    # 재귀 돌면서 같은 것들 다 True로 바꿈
    def recursive(current):
        visited[current] = True
        
        for neighbor in range(n):
            if computers[current][neighbor] == 1 and not visited[neighbor]:
                recursive(neighbor)
    
    for i in range(n):
        if visited[i]:
            continue
        answer += 1
        recursive(i)
        
    return answer
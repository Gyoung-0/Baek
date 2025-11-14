from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    # 해당 노드에 있는 인접한 노드들을 큐에 넣으면서 연결된 모든 노드를 변환 (양방향)
    q = deque()
    
    for i in range(n):
        
        if not visited[i]:
            answer += 1
            q.append(computers[i])
            visited[i] = True
            while q:
                for idx, node in enumerate(q.popleft()):
                    if not visited[idx] and node == 1:
                        q.append(computers[idx])
                        visited[idx] = True
    return answer
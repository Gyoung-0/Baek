from typing import List
def solution(n: int, computers: List[List]) -> int:
    answer = 0
    # 모두 다 한번씩 돌아봐야 하니깐 dfs로
    
    # 방문했는지 확인해야함
    visited: bool = [False] * n

    # 첫번째부터 돌면서 해당 인덱스를 제외한 인덱스의 값이 1이라면 그 인덱스 위치는 연결된걸로 봄
    def dfs(computer: int):
        nonlocal answer
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i)
                print(visited)
        return 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
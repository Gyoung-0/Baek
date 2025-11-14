def solution(tickets):
    # 경로가 2개 이상이면 알파벳 순서
    tickets.sort()
    # 백트래킹
    # 방문한 곳은 재방문 하지 않게
    n = len(tickets)
    visited = [False] * n
    answer = []
    def dfs(route ,loc):
        # route가 n+1개가 되면 끝(모든 도시를 방문할 수 없는 경우는 주어지지 않습니다)
        if len(route) == n+1:
            answer.extend(route)
            return True
        for i in range(n):
            # 출발지와 도착지
            start, end = tickets[i]
            # 출발지랑 현재 위치가 같아야함
            if not visited[i] and start == loc:
                visited[i] = True
                route.append(end)
                # 반복문을 돌다가 끝이나면 종료시킴
                if dfs(route, end):
                    return True
                visited[i] = False
                route.pop()
                
        return False
    dfs(["ICN"], "ICN")
    return answer
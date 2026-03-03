from collections import defaultdict
def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        graph = defaultdict(list)
    
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
            
        visited = set()
        
        def dfs(node):
            visited.add(node)
            count = 1
            
            for next_node in graph[node]:
                if next_node not in visited:
                    count += dfs(next_node)
                    
            return count
        count = dfs(1)

        diff = abs(n-2*count)
        answer=min(answer,diff)
    return answer
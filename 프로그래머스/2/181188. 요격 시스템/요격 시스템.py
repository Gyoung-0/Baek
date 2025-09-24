from collections import deque
def solution(targets):
    # targets을 [0] 기준 오름차순으로 정렬
    
    targets.sort(key=lambda x: x[0])
    targets = deque(targets)
    # 
    count = 0
    answer = 0
    prev = targets.popleft()
    for target in targets:
        if is_inside(prev, target):
            prev[1] = min(prev[1], target[1])
        else: 
            answer += 1
            prev = target
    return answer + 1

def is_inside(prev, after):
    return after[0] < prev[1]
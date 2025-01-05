def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    
    for max_value, min_value in zip(A, B):
        answer += max_value * min_value
    
    return answer
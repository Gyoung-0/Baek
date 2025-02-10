def solution(t, p):
    answer = 0
    t_size = len(t)
    p_size = len(p)
    idx = []
    for i in range(0, t_size-p_size+1):
        comp = int(t[i:i+p_size])
        if comp <= int(p):
            answer += 1
        
        
    return answer
from itertools import combinations
def solution(n, q, ans): 
    answer = 0
    for comb in combinations(range(1, n+1), 5):
        ok = True
        
        for i in range(len(q)):
            count = len(set(comb) & set(q[i]))
            
            if count != ans[i]:
                ok = False
                break
        if ok:
            answer += 1
    return answer
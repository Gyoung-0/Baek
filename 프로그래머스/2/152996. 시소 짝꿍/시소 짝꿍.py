from collections import Counter
def solution(weights):
    answer = 0
    cnt = Counter(weights)
    
    for w in cnt:
        # 같은 무게
        if cnt[w] > 1:
            answer += cnt[w] * (cnt[w]-1) // 2
        
        
        for x,y in [(2,3), (2,4), (3,4)]:
            target = w / x * y
            if target in cnt:
                answer += cnt[w] * cnt[target]
    return answer
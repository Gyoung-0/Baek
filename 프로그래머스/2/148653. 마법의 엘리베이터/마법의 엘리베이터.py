def solution(storey):
    if storey < 10:
        return min(storey, 11 - storey)
    digit = storey % 10
    # 각각 올렸을때 내렸을때 재귀로 비교 몫 + 
    up = 10 - digit + solution(storey // 10 + 1)
    down = digit + solution(storey // 10)
    return min(up, down)
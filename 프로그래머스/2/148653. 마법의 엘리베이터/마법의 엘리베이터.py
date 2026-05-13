def solution(storey):
    answer = 0
    # 각 자리가 5보다 크면 더하고 5보다 작으면 빼서 0으로 만드는게 중요
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10
        if (next_digit >= 5 and digit >= 5) or digit > 5:
            storey += 10
            answer += 10 - digit
        else:
            answer += digit
        
        storey = storey // 10
    return answer
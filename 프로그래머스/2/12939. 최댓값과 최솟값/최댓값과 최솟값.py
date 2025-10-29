def solution(s):
    answer = ''
    numbers = s.split(" ")
    min_ = float('inf')
    max_ = float('-inf')
    for number in numbers:
        if int(number) < min_:
            min_ = int(number)
        if int(number) > max_:
            max_ = int(number)
    
    return f"{min_} {max_}"
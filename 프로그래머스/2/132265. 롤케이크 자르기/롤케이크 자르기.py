from collections import Counter
def solution(topping):
    answer = 0
    press = []
    for x in topping:
        if len(press) < 2 or not (press[-1] == x and press[-2] == x):
            press.append(x)
    
    left = set()
    right = Counter(topping)
    for i in topping:
        left.add(i)
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        if len(left) == len(right):
            answer += 1
            
    return answer
import math
def solution(r1, r2):
    answer = 0
    r1_square = r1*r1
    r2_square = r2*r2
    # r1*r1 <= x*x +y*y <= r2*r2
    # r1*r1 - x*x <= y*y <= r2*r2 - x*x
    for x in range(r2+1):
        y_max = int(math.sqrt(r2*r2 - x*x))
        
        if x < r1:
            y_min = math.ceil(math.sqrt(r1*r1 - x*x))
        else:
            y_min = 0
        answer += y_max - y_min + 1
        
    return answer * 4 - (r2 - r1 +1) * 4
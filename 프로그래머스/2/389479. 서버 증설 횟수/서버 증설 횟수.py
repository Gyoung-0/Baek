import math
def solution(players, m, k):
    # 24개 배열 생성하고, 게임 이용자 수/m 값이 증설된 서버 횟수, 증설 횟수는 처음 증설 될때 +
    server = [0] * 24
    answer = 0
    
    for i in range(24):
        required = players[i] // m
        current = server[i]
        if required > current:
            need = required - current
            answer += need
            
            for j in range(i, min(i + k, 24)):
                server[j] += need
    return answer
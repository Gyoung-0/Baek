import math
def solution(wallpaper):
    answer = []
    # 1. 가장 왼쪽에 있는거 기준으로 거기서 데이터가 있는 가장 위부터 드래그 시작
    # 2. 가장 끝에 있는거 기준으로 거기서 데이터가 있는 가장 아래까지 시작
    left = math.inf
    right = -math.inf
    highst = -1
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            
            if wallpaper[r][c] == '#':
                if highst == -1:
                    highst = r
                if left >  c:
                    left = c
                if right < c:
                    right = c
                lowst = r
    print(highst, left, lowst,right)
    return [highst, left, lowst+1, right+1]
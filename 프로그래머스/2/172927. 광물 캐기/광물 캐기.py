def solution(picks, minerals):
    answer = 0
    # minerals를 돌면서 돌곡괭이 기준 5개씩의 합이 최대가 되는 피로도를 가진곳이 다이아 순으로 들어가고 그 다음 철, 돌 이렇게 하면 될듯
    # 1. minerals의 각 5개씩 피로도 합 구하기
    # 내가 가진 곡괭이로 캘 수 있는 최대 광물 개수까지 자르기
    max_minerals = sum(picks) * 5
    minerals = minerals[:max_minerals]
    total = 0
    arr = []
    order = []
    for i, m in enumerate(minerals):
        if i % 5 == 0 and i > 0:
            order.append((arr ,total))
            arr = []
            total = 0
        if m == "diamond":
            arr.append("diamond")
            total += 25
        elif m == "iron":
            arr.append("iron")
            total += 5
        else:
            arr.append("ston")
            total += 1
        
    if arr:
        order.append((arr ,total))
        arr = []
        stotalum = 0
    # 2. 내림차순으로 다이아, 철, 돌 곡괭이 순으로 분배
    order.sort(key=lambda x: x[1], reverse=True)
    print(order)
    # 3. 다 캐거나, 곡괘잉가 없을때까지 반복문 
    count = 0
    while picks:

        pick = picks.pop(0)
        for i in range(pick):
            if not order:
                break
            li, total = order.pop(0)
            if count == 0:
                    answer += len(li)
            elif count == 1:
                for mineral in li:
                    if mineral == "diamond":
                        answer += 5
                    else:
                        answer += 1
            else:
                for mineral in li:
                    if mineral == "diamond":
                        answer += 25
                    elif mineral == "iron":
                        answer += 5
                    else:
                        answer += 1
        count += 1

    return answer
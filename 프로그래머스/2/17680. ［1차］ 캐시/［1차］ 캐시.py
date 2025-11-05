from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    # 들어있을 경우 +1 안들어있을 경우 +5
    q = deque()
    running_time = 0

    for city in cities:
        city = city.lower()
        if city in q:
            running_time += 1
            q.remove(city)
            q.append(city)
        else:
            running_time += 5
            if len(q) == cacheSize:
                q.popleft()
                q.append(city)
                continue
            q.append(city)

    return running_time
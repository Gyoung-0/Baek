def solution(k, tangerine):
    answer = 0
    # 딕셔너리 만들어서 각 귤 크기마다 개수 넣고 k값 최소값 확인하면 될 거 같은데
    dict = {}
    for tang in tangerine:
        if tang in dict:
            dict[tang] += 1
        else:
            dict[tang] = 1
    sorted_items = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    sum = 0
    for key, value in sorted_items:
        sum += value
        answer += 1
        if sum >= k:
            return answer
    return answer
def solution(s):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    s = list(s)
    arr = []
    while s:
        current = s.pop()
        if not s:
            break
        if arr and arr[-1] == current:
            arr.pop()
        else:
            arr.append(current)
    
    if arr and arr.pop() == current:
        if not arr:
            answer = 1
    return answer
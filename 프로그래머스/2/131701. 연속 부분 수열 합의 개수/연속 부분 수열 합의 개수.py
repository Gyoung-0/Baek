def solution(elements):
    n = len(elements)
    arr = elements * 2  # 원형 처리를 위해 배열 2배로 확장
    prefix = [0] * (2*n + 1)

    # 누적합 만들기
    for i in range(1, 2*n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]

    answer = set()

    # 길이 1 ~ n 까지 부분합
    for length in range(1, n+1):
        for start in range(n):  # 시작점은 원래 배열 크기까지만
            s = prefix[start+length] - prefix[start]
            answer.add(s)

    return len(answer)
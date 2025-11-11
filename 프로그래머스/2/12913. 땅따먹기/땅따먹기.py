def solution(land):
    n = len(land)
    dp = [[0] * len(land[i]) for i in range(n)]
    # dp 리스트 만들기
    dp[0] = land[0][:]
    
    # 1부터 n까지 위에 땅과 비교
    for i in range(1, n):
        for j in range(len(land[i])):
            # 같은 열의 땅을 제외하고 최대값 찾기
            max_ = max(dp[i-1][:j] + dp[i-1][j+1:])
            dp[i][j] = max_ + land[i][j]
            
    return max(dp[-1])
    
    
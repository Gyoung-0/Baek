def solution(board):
    n = len(board)
    m = len(board[0])
    
    # max_side는 정사각형의 최대 변의 길이를 저장합니다.
    max_side = 0
    
    # 1x1 보드인 경우 초기 최대값을 설정 (최대 1)
    # 첫 행과 첫 열은 그 자체가 최대 변의 길이입니다 (DP[i][j] = board[i][j])
    # 따라서 max_side의 초기값은 0 또는 board의 모든 1 중 하나가 될 수 있습니다.
    for row in board:
        max_side = max(max_side, max(row))
    
    # 1행, 1열은 초기값으로 고정되므로, 2행(인덱스 1)과 2열(인덱스 1)부터 시작
    for i in range(1, n):
        for j in range(1, m):
            # 현재 칸의 값이 1일 때만 DP 계산을 수행합니다.
            if board[i][j] == 1:
                # 점화식: min(위, 왼쪽, 왼쪽 위) + 1
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                
                # 현재 계산된 변의 길이와 최대 변의 길이를 비교하여 갱신
                max_side = max(max_side, board[i][j])
                
    # 결과는 가장 큰 정사각형의 '넓이'이므로, 변의 길이를 제곱하여 반환합니다.
    return max_side * max_side
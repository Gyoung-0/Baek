from typing import List
def solution(n: int) -> int:
    answer = 0
    # 체스판 n*n 크기에 체스가 n개씩 들어가면 각 행에 하나씩 같은 열과 대각선만 아니면 됨
    # 인덱스는 체스판의 로우를 값은 컬럼을 나타냄
    board: List[int] = [0] * n
    
    # 해당 열과 행이 그 전 체스말들과 겹치는지 확인
    def is_safe(r: int, c: int) -> bool:
        # 이전 로우들의 체스말들의 위치와 겹치는지 확인
        for prev_row in range(r):
            if board[prev_row] == c:
                return False
            # 대각선의 각 값의 차이가 절대값과 같다면 같은 대각선에 있는 값
            if abs(r - prev_row) == abs(c - board[prev_row]):
                return False
            
        return True
    
    def dfs(row: int):
        nonlocal answer
        
        if row == n:
            answer += 1
        # 해당 로우가 안전한지 확인하면서 False면 
        for i in range(n):
            if is_safe(row, i):
                board[row] = i
                dfs(row+1)
        
        return False
    dfs(0)
    return answer
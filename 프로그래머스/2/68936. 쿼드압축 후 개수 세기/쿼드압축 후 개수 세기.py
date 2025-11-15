from typing import List
def solution(arr: List[List[int]]):
    answer = [0,0]
    n, m = len(arr), len(arr[0]) #행렬
    is_break = False
    def quad(r: int, c: int, size: int):
        start = arr[r][c]
        is_break = False
        # start와 다른 값이 있으면  사각형 분할
        for i in range(r, r+size):
            for j in range(c, c+size):
                if arr[i][j] != start:
                    is_break = True
                    break
            if is_break:
                break

        # 각 4분면 구하기
        if is_break:
            half = size // 2
            quad(r, c, half)
            quad(r+half, c, half)
            quad(r, c+half, half)
            quad(r+half, c+half, half)
        else:
            answer[start] += 1

        
    quad(0,0,n)
    return answer
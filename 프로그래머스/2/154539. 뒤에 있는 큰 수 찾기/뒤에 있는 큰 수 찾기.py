from collections import deque
def solution(numbers):
    answer = []
    # 시간초과 실패
    # n = len(numbers)
    # find = False
    # for i in range(n):
    #     for j in range(i,n):
    #         if numbers[i] < numbers[j]:
    #             answer.append(numbers[j])
    #             find = True
    #             break
    #     if find:
    #         find = False
    #     else:
    #         answer.append(-1)
    
    n = len(numbers)
    answer = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer
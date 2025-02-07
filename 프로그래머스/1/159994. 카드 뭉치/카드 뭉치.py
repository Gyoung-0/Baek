from collections import deque

def solution(cards1, cards2, goal):
    # 큐로 변환
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for word in goal:
        # cards1의 맨 앞 단어가 goal의 단어와 같다면 제거
        if q1 and q1[0] == word:
            q1.popleft()
        # cards2의 맨 앞 단어가 goal의 단어와 같다면 제거
        elif q2 and q2[0] == word:
            q2.popleft()
        # 둘 다 아니라면 올바르게 순서를 맞출 수 없음
        else:
            return "No"
    
    return "Yes"
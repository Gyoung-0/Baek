from collections import deque
def solution(begin, target, words):
    # 가장 짧은 -> BFS
    # 일단 타겟이 words에 있는지 확인
    if not target in words:
        return 0
    # 단어 하나만

    answer_list = [x for x in target]
    begin_list = [x for x in begin]

    q = deque(words)
    answer = 0
    while q:
        word_list = [x for x in q.popleft()]
        count = 0
        for i in range(len(word_list)):
            if answer_list[i] == begin_list[i]:
                count += 1
        
        if count == len(word_list) - 1:
            return answer +1
        count = 0
        for i in range(len(word_list)):
            if word_list[i] == begin_list[i]:
                count += 1
        
        if count == len(word_list) - 1:
            begin_list = word_list
            answer += 1  
    return answer
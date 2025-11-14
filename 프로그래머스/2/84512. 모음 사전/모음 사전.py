def solution(word):
    #그냥 다 채우고 정렬하면 되는거 아닌가
    word_list = set()
    word_collections = ['A', 'E', 'I', 'O', 'U']
    # 재귀로 길이가 5까지 A E I O U 하나씩 모두 채우기
    def dfs(n):
        if len(n) == 5:
            return True
        for i in word_collections:
            word_list.add(n+i)
            dfs(n+i)
        return False
    dfs("")
    answer = sorted(word_list)
    for i, w in enumerate(answer):
        if word == w:
            return i+1
    return 0
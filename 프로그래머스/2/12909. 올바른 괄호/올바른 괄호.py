def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        
        if s[i] == '(':
            stack.append(s[i])
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return not stack
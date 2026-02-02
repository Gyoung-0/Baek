def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        if word == '':
            answer += ' '
            continue
        
        word = word[0].upper() + word[1:].lower()
        answer = answer + " " + word
        
    return answer.lstrip()
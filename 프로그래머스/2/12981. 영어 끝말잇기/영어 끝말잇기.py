def solution(n, words):
    answer = []
    repeat = 1
    count = 1
    previous_words = set()
    last_word = (words[0])[-1]
    previous_words.add(words[0])
    for word in words[1:]:
        count += 1
        if count > n:
            count = 1
            repeat += 1
            
        first_word = word[0]
            
        if first_word != last_word:
            return [count, repeat]
        
        if word in previous_words:
            return [count, repeat]
        
        previous_words.add(word)
        last_word = word[-1]
        

        

    return [0, 0]
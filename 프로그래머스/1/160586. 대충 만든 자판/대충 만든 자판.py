def solution(keymap, targets):
    key_dict = {}
    answer = []
    for key_idx, key in enumerate(keymap):
        for press_count, char in enumerate(key , start=1):
            if char in key_dict:
                key_dict[char] = min(key_dict[char], press_count)
            else:
                key_dict[char] = press_count
        
    for target in targets:
        total = 0
        for t in target:
            if not t in key_dict:
                total = -1
                break
            else:
                total += key_dict[t]
        answer.append(total)
    return answer
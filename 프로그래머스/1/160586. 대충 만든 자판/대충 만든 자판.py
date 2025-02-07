def solution(keymap, targets):
    # 1. 각 문자에 대해 최소 입력 횟수 저장하는 딕셔너리 생성
    key_dict = {}

    for key_idx, key in enumerate(keymap):
        for press_count, char in enumerate(key, start=1):  # 1부터 시작
            if char in key_dict:
                key_dict[char] = min(key_dict[char], press_count)  # 최소 입력 횟수 갱신
            else:
                key_dict[char] = press_count

    answer = []
    
    # 2. 각 target 단어에 대해 최소 입력 횟수 계산
    for target in targets:
        total_presses = 0  # 해당 단어를 입력하는 총 횟수
        
        for char in target:
            if char in key_dict:
                total_presses += key_dict[char]  # 해당 문자의 최소 입력 횟수를 더함
            else:
                total_presses = -1  # 하나라도 입력 불가능한 문자가 있으면 -1
                break
        
        answer.append(total_presses)  # 결과 저장

    return answer
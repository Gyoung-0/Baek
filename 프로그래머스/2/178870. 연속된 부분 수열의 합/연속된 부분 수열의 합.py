def solution(sequence, k):
    left = 0
    right = 0
    sum_val = sequence[0]
    min_len = float('inf')
    answer = []
    
    while right < len(sequence):
        if sum_val  == k:
            if (right - left) < min_len:
                min_len = right -left
                answer = [left, right]
            sum_val -= sequence[left]
            left += 1
        elif sum_val < k:
            right += 1
            if right < len(sequence):
                sum_val += sequence[right]
        else:
            sum_val -= sequence[left]
            left += 1
    return answer


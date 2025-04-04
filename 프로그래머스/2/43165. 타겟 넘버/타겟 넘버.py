def solution(numbers, target):
    answer = recursive(numbers,0,0,target)
    return answer


def recursive(numbers, idx, current_sum, target):
    if idx == len(numbers):
        if(current_sum == target):
            return 1
        else:
            return 0

    num = numbers[idx]
    positive_sum = recursive(numbers, idx + 1, current_sum + num, target)
    negative_sum = recursive(numbers, idx + 1, current_sum - num, target)
    return positive_sum + negative_sum
    
        
        
def solution(numbers, target):
    answer = 0
    def recursive(idx, current):
        if idx == len(numbers):
            if target == current:
                return 1
            return 0
        
        num = numbers[idx]
        
        return recursive(idx+1, current+num) + recursive(idx+1, current-num)
    
    return recursive(0, 0)
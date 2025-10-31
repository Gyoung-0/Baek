def solution(n):
    answer = []
    # 3진법인데 3으로 나눠질때는 몫-1으로하고 4로 바꿔야함
    numbers = ['4', '1', '2']
    while n>0:
        remainder = n % 3
        answer.append(numbers[remainder])
        
        if remainder == 0:
            n = (n // 3) - 1
        else:
            n =  n // 3
        

    return "".join(answer[::-1])
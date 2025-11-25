def solution(n,a,b):
    answer = 0
    # (각 참가자 번호 + 1) // 2 값이 다음 번호 
    # (각 참가자 번호 + 1) // 2 가 A,B 모두 같다면 붙은것
    while n // 2 != 0:
        a = (a+1) // 2
        b = (b+1) // 2
        if a == b:
            return answer+1
        
        answer += 1
        n /= 2
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
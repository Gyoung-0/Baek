def solution(diffs, times, limit):
    # 퍼즐의 난이도= diff, 현재 퍼즐의 소요시간 = time_cur, 이전 퍼즐 소요시간 = time_prev, 숙련도=level
    # diff <= level -> time_cur 만큼 사용해 해결
    # diff > level -> diff - level 번 틀림 (틀릴때마다 time_cur만큼 시간 사용), 
    #   추가로 time_prev만큼 시간 사용해 이전 퍼즐 다시 품
    #   이전 퍼즐을 풀때는 난이도 상관없이 틀리지 않음 (diff-level번 틀린 이후 풀면 time_cur만큼의 시간 사용해 해결)
    
    # 1부터 시작해 limit의 최댓값이 넘어가기 전 값을 result로 하면 그때 시간복잡도는?
    # diff 최댓값부터 시작헤 1씩 줄여가면서  limit이 최대인값 찾으면 그때 시간복잡도는?
    n = len(diffs) 
    # divide and conquer로 해결
    def can_clear(level):
        prev_time = 0
        total_time = 0

        for i in range(n):
            diff = diffs[i]
            time_cur = times[i]

            if diff <= level:
                total_time += time_cur
            else:
                if i == 0:
                    total_time += time_cur
                else:    
                    total_time += (diff-level) * (time_cur + prev_time) + time_cur

            if total_time > limit:
                return False

            prev_time = time_cur
        return True

    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_clear(mid):
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    return answer
    

    


    
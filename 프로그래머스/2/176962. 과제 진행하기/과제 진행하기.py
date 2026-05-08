def solution(plans):
    answer = []
    for i in range(len(plans)):
        subject, time, takes = plans[i]
        h, m = map(int, time.split(':'))
        plans[i] = (subject, h*60 + m, int(takes))
        
    plans.sort(key=lambda x: x[1])
    
    stack = []
    
    for i in range(len(plans)-1):
        subject, start, takes = plans[i]
        next_start = plans[i+1][1]
        
        remain_time = next_start - start
        
        if remain_time >= takes:
            answer.append(subject)
            remain_time -= takes
            
            while stack and remain_time > 0:
                prev_subject, prev_time = stack.pop()
                if remain_time >= prev_time:
                    remain_time -= prev_time
                    answer.append(prev_subject)
                else:
                    stack.append((prev_subject, prev_time - remain_time))
                    break
        else:
            stack.append((subject, takes - remain_time))
    answer.append(plans[-1][0])
    
    while stack:
        answer.append(stack.pop()[0])
    return answer
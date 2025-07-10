def solution(book_time):
    max_minutes = 24 * 60
    timeline = [0] * (max_minutes + 10)
    
    for start_str, end_str in book_time:
        start_minute = int(start_str.split(':')[0]) * 60 + int(start_str.split(':')[1])
        end_minute = int(end_str.split(':')[0]) * 60 + int(end_str.split(':')[1])
        
        for i in range(start_minute, end_minute + 10): 
            timeline[i] += 1 
            
    return max(timeline)
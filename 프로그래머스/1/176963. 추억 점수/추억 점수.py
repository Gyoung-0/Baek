def solution(name, yearning, photo):
    answer = []
    for group in photo:
        point = [name.index(person) for person in group if person in name]
        total_score = sum(yearning[idx] for idx in point)
        answer.append(total_score)
    return answer
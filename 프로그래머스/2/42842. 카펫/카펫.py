def solution(brown, yellow):
    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h == 0:           # 약수 발견
            w = yellow // h           # 짝 약수

            total_w = w + 2
            total_h = h + 2

            if 2 * (total_w + total_h) - 4 == brown:
                return [total_w, total_h]
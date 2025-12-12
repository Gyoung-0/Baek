def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        curr = phone_book[i]
        next_num = phone_book[i+1]

        if len(next_num) < len(curr):
            continue

        is_prefix = True
        for idx in range(len(curr)):
            if curr[idx] != next_num[idx]:
                is_prefix = False
                break

        if is_prefix:
            return False

    return True
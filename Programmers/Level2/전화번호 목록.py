def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book, key=lambda x: len(x))

    for i, phone_num in enumerate(phone_book):
        prefix_set = set()

        for other_phone_num in phone_book[i + 1:]:
            prefix_set.add(other_phone_num[:len(phone_num)])

        if phone_num in prefix_set:
            answer = False
            break

    return answer


print(solution(["12232332", "12", "222222"]))

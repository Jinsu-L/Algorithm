import math


def solution(n, a, b):
    answer = 0
    a, b = min(a, b), max(a, b)
    for i in range(int(math.log2(n)) + 1):
        answer += 1
        if a + 1 == b:
            break

        a, b = math.ceil(a / 2), math.ceil(b / 2)

    return answer


print(solution(8, 4, 7))

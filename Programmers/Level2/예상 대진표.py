import math


def solution(n, a, b):
    answer = 0
    a, b = min(a, b), max(a, b)
    for i in range(int(math.log2(n))):
        answer += 1
        if a%2 != 0 and a + 1 == b:
            break

        a, b = math.ceil(a / 2), math.ceil(b / 2)

    return answer


print(solution(8, 2, 3))

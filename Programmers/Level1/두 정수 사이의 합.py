def solution(a, b):
    a, b = (a, b) if a < b else (b, a)
    answer = sum([i for i in range(a, b + 1)])
    return answer


print(solution(5, 3))

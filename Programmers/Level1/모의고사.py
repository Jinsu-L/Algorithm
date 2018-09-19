def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    thrid = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    i = 0
    f = 0
    s = 0
    t = 0
    for ans in answers:
        f += first[i % len(first)] == ans
        s += second[i % len(second)] == ans
        t += thrid[i % len(thrid)] == ans
        i += 1

    scores = [f, s, t]
    answer = []
    max = 0
    for i, score in enumerate(scores):
        if max < score:
            max = score
            answer.clear()
            answer.append(i + 1)
        elif max == score:
            answer.append(i + 1)

    return answer


print(solution([1, 3, 2, 4, 2]))
print(solution([1, 2, 3, 4, 5]))

'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
'''

def solution(s):
    answer = 0

    for idx, number in enumerate(s[::-1]):
        if number == '-':
            answer *= -1
        else:
            answer += int(number) * (10 ** idx)
    return answer

print(solution("-1234"))
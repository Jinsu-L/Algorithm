def solution(s):
    i = 0
    answer = ''
    for c in s:
        if c == ' ':
            i = 0
            answer += ' '
        else:
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
            i += 1

    return answer


print(solution("try hello world"))

def solution(n):
    answer = ''

    while(n > 0):
        n, nmg = divmod(n, 3)
        if nmg == 0:
            n -= 1
        answer = "412"[nmg] + answer

    return answer


print(solution(4))
print(solution(5))

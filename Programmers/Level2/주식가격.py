def solution(prices):
    answer = []

    for i in range(len(prices)):
        now = prices[i]
        duration = 0
        for j in range(i + 1, len(prices)):
            cur = prices[j]
            duration += 1
            if now > cur:
                answer.append(duration)
                break
        else:
            answer.append(duration)
    return answer

print(solution([1, 2, 3, 2, 3]))

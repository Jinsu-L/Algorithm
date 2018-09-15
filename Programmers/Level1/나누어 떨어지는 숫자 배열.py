def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    answer = answer if len(answer) else [-1]
    return answer


print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))

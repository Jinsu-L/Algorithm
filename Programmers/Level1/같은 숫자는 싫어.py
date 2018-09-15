def solution(arr):
    answer = [arr[0]] + [arr[n] for n in range(1, len(arr)) if arr[n - 1] != arr[n]]

    return answer


def other_solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer


print(solution([3, 4, 4, 3, 3]))
print(other_solution([3, 4, 4, 3, 3]))

# 에라토스테네스의 체

def solution(n):
    arr = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if arr[i] != 0:
            for j in range(i + i, n + 1, i):
                arr[j] = 0

    return len(arr) - arr.count(0) - 1


print(solution(10))

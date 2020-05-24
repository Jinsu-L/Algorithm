def solution(cookie):
    answer = 0

    for m in range(1, len(cookie)):
        l = 0
        r = len(cookie)
        cur_max = 0
        left = sum(cookie[l:m])
        right = sum(cookie[m: r])
        while (l < m and r > m):
            if left == right:
                cur_max = left
                break

            if left < right:
                r -= 1
                right -= cookie[r]
            else:
                left -= cookie[l]
                l += 1

        if cur_max > answer:
            answer = cur_max

    return answer


print([1, 1, 2, 3])
print(solution([1, 1, 2, 3]))
print(solution([1, 2, 4, 5]))

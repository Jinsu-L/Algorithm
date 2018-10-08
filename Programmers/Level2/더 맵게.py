# 스코빌 지수를 K 이상으로 만들고 싶음
# 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq


def solution(scoville, K):
    answer = 0

    q = []
    for i in scoville:
        heapq.heappush(q, i)

    while (True):
        min_scoville = heapq.heappop(q)
        if min_scoville >= K:
            break

        if len(q) == 0:
            return -1

        next_scoville = heapq.heappop(q)

        heapq.heappush(q, min_scoville + (next_scoville * 2))
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1,2], 3))

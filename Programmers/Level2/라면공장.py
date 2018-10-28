import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    q = []

    # heapq.heappush(q, stock)

    start = 0
    while (stock < k):
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(q, supplies[i])
            else:
                start = i
                break

        answer += 1
        stock += heapq._heappop_max(q)

    return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))

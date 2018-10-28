import queue
import sys
sys.setrecursionlimit(10 ** 5)
sys.api_version
def solution(n, computers):
    answer = 0

    visited = [0 for i in range(n)]

    for i in range(n):
        if visited[i] == 0:
            q = queue.Queue()

            q.put(i)

            while (not q.empty()):
                x = q.get()

                for y in range(n):
                    if computers[x][y] != 0 and visited[y] == 0:
                        visited[y] = 1
                        q.put(y)

            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

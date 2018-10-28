def solution(baseball):
    answer = 0

    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                for k in range(1, 10):
                    if k not in (i, j):
                        num = str(i * 100 + j * 10 + k)
                        test = True
                        for q in baseball:
                            s = 0
                            b = 0
                            q_num = str(q[0])
                            for index in range(3):
                                if num[index] == q_num[index]:
                                    s += 1
                                for ball_index in range(3):
                                    if index != ball_index:
                                        if num[index] == q_num[ball_index]:
                                            b += 1

                            if s != q[1] or b != q[2]:
                                test = False
                                break
                        if test:
                            answer += 1

    return answer


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))

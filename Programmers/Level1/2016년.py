def solution(a, b):
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = sum(month[:a-1]) + b
    answer = week[day % 7]
    return answer


print(solution(5, 24))

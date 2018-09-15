def solution(seoul):
    for i, s in enumerate(seoul):
        if s == "Kim":
            return "김서방은 {}에 있다".format(i)


print(solution(["Jane", "Kim"]))
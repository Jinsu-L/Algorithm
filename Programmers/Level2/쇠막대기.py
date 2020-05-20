def solution(arrangement):
    answer = 0
    arrangement = arrangement.replace("()", "0")

    stack = list()
    for bracket in arrangement:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            stack.pop()
            answer += 1
        else:
            answer += len(stack)

    return answer


print(solution("()"))
print(solution("(())"))
print(solution("(()())"))
print(solution("()(((()())(())()))(())"))

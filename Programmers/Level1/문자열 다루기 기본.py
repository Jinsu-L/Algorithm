def solution(s):
    answer = s.isnumeric() and (len(s) in (4, 6))
    return answer


print(solution("a234"))

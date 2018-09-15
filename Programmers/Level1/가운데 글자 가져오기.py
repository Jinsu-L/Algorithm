def solution(s):
    l = len(s)
    st, e = (l // 2, l // 2 + 1) if l % 2 else (l // 2 - 1, l // 2 + 1)
    answer = s[st: e]
    return answer


print(solution("abcde"))
print(solution("qwer"))

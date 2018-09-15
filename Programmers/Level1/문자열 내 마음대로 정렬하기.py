def solution(strings, n):
    strings = sorted(strings)
    answer = sorted(strings, key=lambda strings: strings[n])
    return answer


print(solution(["abce", "abcd", "cdx"], 2))

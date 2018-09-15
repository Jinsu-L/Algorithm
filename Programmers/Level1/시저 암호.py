def solution(s, n):
    answer = ''
    t = [ord(i) for i in s]
    for i in t:
        if i == 32:
            answer += chr(i)
        elif i < 91:
            answer += (chr(i + n) if i + n < 91 else chr(i - (26 - n)))
        else:
            answer += (chr(i + n) if i + n < 123 else chr(i - (26 - n)))

    return answer


for i in range(1, 26):
    print(solution("abcdefghijklmnopqrstuvwxyz".upper(), i))

"""
a 97
z 122
A 65
Z 90
"""

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a

def solution(n):
    answer = fibonacci(n) % 1234567
    return answer

print(solution(5))
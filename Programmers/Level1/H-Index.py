def solution(citations):
    citations = sorted(citations, reverse=True)
    print(citations)
    for i, citation in enumerate(citations):
        if citations[i] <= i:
            return citations[i]
    return 0


print(solution([2,1 ]))

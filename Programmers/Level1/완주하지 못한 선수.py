def solution(participant, completion):
    hash_dict = dict()

    for man in participant:
        if not man in hash_dict:
            hash_dict[man] = 1
        else:
            hash_dict[man] += 1

    for man in completion:
        hash_dict[man] -= 1

    answer = [name for name, value in hash_dict.items() if value == 1][0]

    return answer

import collections
def other_solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(other_solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

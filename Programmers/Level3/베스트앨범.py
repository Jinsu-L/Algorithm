def solution(genres, plays):
    answer = []
    hash_map = {}

    play_list = list(zip(genres, enumerate(plays)))

    for genre, plays in play_list:
        if genre in hash_map:
            temp = hash_map[genre]
            temp[0] += plays[1]
            temp.append(plays)
            hash_map[genre] = temp
        else:
            hash_map[genre] = [plays[1], plays]
    values = hash_map.values()
    values = sorted(values, reverse=True)

    for tmp_list in values:
        sorted_list = sorted(tmp_list[1:], key=lambda x: x[1], reverse=True)
        for j in range(2 if len(sorted_list) >= 2 else len(sorted_list)):
            answer.append(sorted_list[j][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

def solution(clothes):
    answer = 1

    hash_map = {}

    for cloth_name, cloth_cate in clothes:

        if cloth_cate in hash_map:
            hash_map[cloth_cate] += 1
        else:
            hash_map[cloth_cate] = 1

    for i in hash_map.values():
        answer *= i + 1
    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

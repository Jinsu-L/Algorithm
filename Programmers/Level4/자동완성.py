class Node:
    def __init__(self, c):
        self.possible_words = 1
        self.char = c
        self.nexts = dict()
        self.compl_word = ""

    def add_next(self, next_node):
        self.nexts[next_node.char] = next_node

    def get_next_chars(self):
        return self.nexts.keys()

    def get_next_char(self, c):
        return self.nexts[c]

def solution(words):
    answer = 0

    bucket = dict()
    # make trie
    for word in words:
        prev_node = None
        for c in word:
            if prev_node is None:
                if c in bucket:
                    prev_node = bucket[c]
                    prev_node.possible_words += 1
                    continue
                else:
                    cur_c = Node(c)
                    bucket[c] = cur_c
                    prev_node = cur_c
                    continue

            if c in prev_node.get_next_chars():
                cur_c = prev_node.get_next_char(c)
                cur_c.possible_words += 1
                prev_node = cur_c
            else:
                cur_c = Node(c)
                prev_node.add_next(cur_c)
                prev_node = cur_c

        prev_node.compl_word = word

    # check word prefix
    for word in words:
        cur = None
        depth = 0
        for c in word:
            depth += 1
            if cur is None:
                cur = bucket[c]
            else:
                cur = cur.get_next_char(c)

            if cur.possible_words == 1:
                break

        answer += depth

    return answer


print(solution(['go', 'gone', 'guild']))
print(solution(['abc', 'def', 'ghi', 'jklm']))
print(solution(['word', 'war', 'warrior', 'world']))

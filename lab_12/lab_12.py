from collections import defaultdict

def find_anagrams(strings):
    anagram_groups = defaultdict(list)

    for idx, word in enumerate(strings):
        key = ''.join(sorted(word))
        anagram_groups[key].append(idx + 1)  # индексы с 1

    # Группы отсортированы по первому индексу
    sorted_groups = sorted(anagram_groups.values(), key=lambda x: x[0])

    # В каждой группе отсортируем индексы
    for group in sorted_groups:
        group.sort()

    return sorted_groups


# Пример использования
def test():
    n = 6
    strings = ["silent", "listen", "banana", "abc", "cab", "bac"]
    result = find_anagrams(strings)
    for group in result:
        print(' '.join(map(str, group)))

# Ожидаемый вывод:
# 1 2
# 3
# 4 5 6

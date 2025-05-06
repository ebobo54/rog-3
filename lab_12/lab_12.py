from collections import defaultdict

def find_anagrams():
    n = int(input())
    strings = input().split()


    anagrams = defaultdict(list)


    for idx, s in enumerate(strings):
        sorted_s = ''.join(sorted(s))  
        anagrams[sorted_s].append(idx)  

    result = []
    for group in anagrams.values():
        result.append(" ".join(map(str, sorted(group))))  

    result.sort(key=lambda x: int(x.split()[0]))
    for group in result:
        print(group)

if __name__ == '__main__':
    find_anagrams()

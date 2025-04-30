def quick_sort(participants, low, high):
    if low < high:
        pivot_index = partition(participants, low, high)
        quick_sort(participants, low, pivot_index)
        quick_sort(participants, pivot_index + 1, high)

def partition(participants, low, high):
    pivot = participants[(low + high) // 2]
    while True:
        while compare(participants[low], pivot) < 0:
            low += 1
        while compare(participants[high], pivot) > 0:
            high -= 1
        if low >= high:
            return high
        participants[low], participants[high] = participants[high], participants[low]
        low += 1
        high -= 1

def compare(a, b):
    if a[1] != b[1]:
        return -1 if a[1] > b[1] else 1
    if a[2] != b[2]:
        return -1 if a[2] < b[2] else 1
    return -1 if a[0] < b[0] else (1 if a[0] > b[0] else 0)

n = int(input())
participants = []
for _ in range(n):
    name, p, f = input().split()
    participants.append((name, int(p), int(f)))

quick_sort(participants, 0, len(participants) - 1)

for p in participants:
    print(p[0])

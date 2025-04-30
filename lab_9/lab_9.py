def merge(arr, lf, mid, rg):
    result = []
    i = lf
    j = mid
    while i < mid and j < rg:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1
    result.extend(arr[i:mid])
    result.extend(arr[j:rg])
    for k in range(len(result)):
        arr[lf + k] = result[k]
    return result

def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)

def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a[:], 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected, f"Expected {expected}, got {b}"

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected, f"Expected {expected}, got {c}"

if __name__ == '__main__':
    test()

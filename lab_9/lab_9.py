def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    
    i = j = 0
    k = lf
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, lf, rg):
    if rg - lf > 1:
        mid = (lf + rg) // 2
        
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        
        merge(arr, lf, mid, rg)

def test():
    a = [1, 4, 9, 2, 10, 11]
    merge(a, 0, 3, 6) 
    expected = [1, 2, 4, 9, 10, 11]
    assert a == expected, f"Expected {expected}, but got {a}"

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected, f"Expected {expected}, but got {c}"

if __name__ == '__main__':
    test()
    print("Tests passed successfully!")

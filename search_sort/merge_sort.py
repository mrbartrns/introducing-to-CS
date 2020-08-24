def merge(left: list, right: list):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 남은 것 처리
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_recur(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_recur(arr[:middle])
        right = merge_recur(arr[middle:])
        return merge(left, right)

a = [8, 4, 1, 6, 5, 9, 2, 0]

print(merge_recur(a))

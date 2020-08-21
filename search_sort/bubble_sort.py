def bubble_sort(arr: list)->list:
    # bubble sort is compare two elements between j and j-1 indexes, and swap if j-1 > j
    swap: bool = False
    while not swap:
        swap = True
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                swap = False
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr

arr = [5, 3, 7, 1, 9]

print(bubble_sort(arr))

# practice
def bubble(arr):
    swap = False
    while not swap:
        for j in range(1, len(arr)):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
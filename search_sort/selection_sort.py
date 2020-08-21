def selection_sort(arr:list) -> list:
    #selection sort is simillar to bubble sort but swap it with element at index 0
    suffixSt = 0
    while suffixSt != len(arr):
        for i in range(suffixSt, len(arr)):
            if arr[i] < arr[suffixSt]:
                arr[suffixSt], arr[i] = arr[i], arr[suffixSt]
        suffixSt += 1
    return arr

arr = [5, 3, 7, 1, 9]

print(selection_sort(arr))

# Difference between two functions?
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
    return L

def sel(arr):
    for i in range(len(arr) - 1):
        minIdx = i
        minVal = arr[i]
        j = i + 1
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                minIdx = j
                minVal = arr[j]
            j += 1
        if minIdx != i:
            temp = arr[i]
            arr[i] = arr[minIdx]
            arr[minIdx] = temp

def new_Sort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
    return L

# selSort only does one "swap" each iteration of i, but newSort may use up to (n-i) "swaps" for each iteration of i.

# Difference between two functions?
# Bubble sort
def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

# Selection sort
def newSort(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
    return L
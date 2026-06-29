'''Rotate list by k positions'''
#example
arr = [1, 2, 3, 4, 5]
k = 2

def rotate_list(arr, k):
    n = len(arr)
    k = k % n
    if k == 0:
        return arr
    return arr[-k:] + arr[:-k]

print(rotate_list(arr, k))  # [4, 5, 1, 2, 3]

def rotate_list_inplace(arr, k):
    n = len(arr)
    k = k % n
    if k == 0:
        return
    arr[:] = arr[-k:] + arr[:-k]

print(rotate_list_inplace(arr, k))  # [4, 5, 1, 2, 3]

def rotate_list_optimized(arr, k):
    n = len(arr)
    k = k % n
    if k == 0:
        return
    arr[:] = arr[-k:] + arr[:-k]

print(rotate_list_optimized(arr, k))  # [4, 5, 1, 2, 3]

def rotate_list_optimized(arr, k):
    n = len(arr)
    k = k % n
    if k == 0:
        return
    arr[:] = arr[-k:] + arr[:-k]

print(rotate_list_optimized(arr, k))  # [4, 5, 1, 2, 3]
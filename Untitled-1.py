def merege(arr1, arr2, m, n):
    j = 0
    k = 0
    arr = []

    while (j < m and k < n):
        if arr1[j] < arr2[k]:
            arr.append(arr1[j])
            j += 1
        else:
            arr.append(arr2[k])
            k += 1
    while j < m:
        arr.append(arr1[j])
        j += 1
    while k < n:
        arr.append(arr2[k])
        k += 1

    return arr


def mergeshort(arr, l, r):
    if l < r:
        mid = l + ((r - l) // 2)

        mergeshort(arr, l, mid)
        mergeshort(arr, mid, r)
        merege(arr)

# This also works on the divide and conquer principle. The idea is to select a pivot element from the array and partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

def QuickSort(arr, l, r):
    if(l < r):
        p = partition(arr, l , r)

        QuickSort(arr, l , p-1)
        QuickSort(arr, p+1 , r)

def partition(arr, l, r):
    pivot = arr[l]

    i = l +1
    j = r

    while True:
        while(i < j and arr[i] < pivot):
            i = i +1

        while(i < j and arr[j] > pivot):
            j = j- 1

        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l] , arr[j] = arr[j] , arr[l]

    return j

arr = [10, 30, 22, 8, 15, 45]
QuickSort(arr, 0 , len(arr) - 1)
print(arr)


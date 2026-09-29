def find_min_max(arr, start , end):
    if (start == end):
        return arr[start] , arr[end]   # when arr have only 1 element 
    
    if (start + 1 == end):             # when arr have only 2 element 
        if (arr[start] < arr[end]):
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]

    mid = (start + end) // 2 

    min1, max1 = find_min_max(arr, start, mid)
    min2, max2 = find_min_max(arr, mid+1 , end)

    return min(min1, min2) , max(max2, max1)

arr = [20, 4, 55, 27, 34, 45, 79]
min_va, max_va = find_min_max(arr, 0, len(arr) -1)
print("Min value : " , min_va)
print("Max Value : " , max_va)

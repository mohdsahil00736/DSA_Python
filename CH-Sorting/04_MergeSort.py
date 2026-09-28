# First we have to apply the divide and conquer method in merger sort 

def Divide(arr, l , r):

    if (l < r ):
        mid = (l+r)//2
        Divide(arr, l , mid)
        Divide(arr, mid +1 , r)
        merge(arr, l, mid , r)

def merge(arr, l , mid , r):
    Size_p1 = mid -l + 1    # size means -> last - start + 1  
    Size_p2 = r - mid       # here -> r - (mid + 1) + 1

    L_arr = [0] * Size_p1    # Left subarray for storing the values
    R_arr = [0] * Size_p2    # Right subarray for storing the values

    for i in range(Size_p1):
        L_arr[i] = arr[l + i]

    for j in range(Size_p2):
        R_arr[j] = arr[(mid + 1) + j]

    i = j = 0 
    k = l 

    while(i < Size_p1 and j < Size_p2):
        if (L_arr[i] < R_arr[j]):
            arr[k] = L_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = R_arr[j]
            j += 1
            k += 1

    while(i < Size_p1):
        arr[k] = L_arr[i]
        i += 1
        k += 1
    while(j < Size_p2):
        arr[k] = R_arr[j]
        j += 1
        k += 1

           

arr = [10, 30, 22, 8, 15, 45]
Divide(arr, 0 , len(arr) - 1)
print(arr)
# find the min max of the array using greedy approach

def diff_min_max(arr):

    arr.sort()
    n = len(arr)
    mid = n //2
    min = 0 
    max = 0 
    j = n-1

    for i in range(mid):
        max = max + abs(arr[i] - arr[j])   # for max value we take the difference of the first and last element
        j = j - 1

        min = min + abs(arr[2*i] - arr[2*i +1]) # for min vlaue , take the diff of adjacent elements

    print("min value : " , min)
    print("max vlaue : ", max)


arr = [12, 5, 25, 10, 2, 15, 8, 30]
diff_min_max(arr)

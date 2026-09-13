from array import *
# Iterative apporach of sum the number 
arr = array('i', [1, 2, 3, 4, 5,6,7])

def Sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(Sum_iterative(arr))

# recursive Approach of sum of the number 

def Sum_recursive(arr):
    if not arr :
        return 0    # Base case 
    return arr[0] + Sum_recursive(arr[1:])  # Recursive call 

print(Sum_recursive(arr))


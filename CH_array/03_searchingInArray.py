from array import * 

arr = array('i', [12, 44, 56, 78, 90, 102])

i = arr.index(12)
print(i)

p = arr.index(1000) # gives error not present in array
print(p)
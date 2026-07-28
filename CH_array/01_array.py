# import array as arr
# Different ways to import array 
from array import *

val = array('i', [1, 2, 3, 4, 5])
print(val)


for i in range(0,5):
    print(val[i], end = " ")

print("\n")
for x in val:
    print(x, end = " , ")

print('\n')
val2 = array('u', ["a", "b", "c"])
for i in range(0, len(val2)):
    print(val2[i], end = " ")

print('\n')
print(val.typecode)
print('\n')
val.reverse()
for i in range(0 , len(val)):
    print(val[i], end = " ")

print("\n")
copy_in_new_array = array(val.typecode, (x*2 for x in val))

copy_in_new_array.insert(2, 23)
copy_in_new_array.pop()
copy_in_new_array.remove(10)
for i in range(0, len(copy_in_new_array)):
    print(copy_in_new_array[i], end = " ")
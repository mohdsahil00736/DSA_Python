from array import * 

arr = array("i", [])

n = int(input("Enter the Array size "))

for i in range(0, n):
    arr.append(int(input("Enter the input number ")))

for x in arr:
    print(x , end= " ")
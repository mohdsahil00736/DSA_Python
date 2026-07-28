from numpy import * 

val = array([1 ,2 ,3, 4.5, "a"])  # Hetrogeneous array
for i in range(0, len(val)):
    print(val[i], end = " ")

print('\n')
val2 = array([1,2,3], float)
for x in val2:
    print(x, end = " ")

print('\n')
val3 = linspace(10, 30 , 5)   # (Start , end , equal part)
for x in val3:
    print(x , end= " ")

print('\n')
val4 = arange(10, 30, 2)  # (Strt , End , Common Difference)
for x in val4:
    print(x , end="")

print('\n')
val5 = logspace(10, 20 , 2)  # print in form of log or e kay power my 
for x in val5:
    print(x, end=" ")

print('\n')
val6 = zeros(5)  # print input time zeros (0 ) / ones ( 1 )
for x in val6:
    print(x, end=" ")

print('\n')
val7 = full(10 , 5)    # first size -> 10, then number -> 5 =>  10 times 5 
for x in val7:
    print(x , end=" ")
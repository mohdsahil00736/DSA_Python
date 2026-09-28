def BubbleSort(a):
    n = len(a)   # any array or list -> a
    for i in range(n):
        for j in range(n-1-i):
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

# a = list(map(int, input("Enter the number to sort : ").split()))
a = [4, 3, 8 , 9]
BubbleSort(a)
print(a)
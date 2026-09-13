
# # Factorial By Loop
# num = int(input(("Enter the number : ")))
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
#     i = i + 1
# print(f"Factorial of the {num} : {fact}")


# # Factorial By Recursion
# num2 = int(input("Enter the Number again : "))
# fact2 = 1
# def factorial(num2):
#     if (num2 == 0 or num2 == 1):
#         return 1
#     return (num2 * factorial(num2 -1))

# print(factorial(num2))

# Fibonaci By Recursion
num3 = int(input("Enter the number for Fibonaci : "))
fib = 0
def fibonaci(num3):
    if (num3 == 1 or num3 == 2):
        return 1
    else:
        return fibonaci(num3-1) + fibonaci(num3-2)
print(fibonaci(num3))



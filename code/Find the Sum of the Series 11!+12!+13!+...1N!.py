
# Q-69. Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+...1/N!

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_series(n):
    series_sum = 0
    for i in range(1, n + 1):
        series_sum += 1 / factorial(i)
    return series_sum


N = int(input("Enter the value of N: "))

if N < 0:
    print("Please enter a non-negative integer.")
else:
    result = sum_of_series(N)
    print("The sum of the series 1/1! + 1/2! + 1/3! + ... + 1/N! is: ",result)


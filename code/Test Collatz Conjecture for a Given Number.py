
# Q-63. Python Program to Test Collatz Conjecture for a Given Number

def collatz_conjecture(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)


num = int(input("Enter a positive integer: "))

print(f"Collatz sequence for :",num)
collatz_conjecture(num)

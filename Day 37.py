#factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial (6))

#Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))


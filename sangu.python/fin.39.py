def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence
n = 10
result = fibonacci(n)
print("2213711058039")
print(f"Fibonacci sequence of the first {n} numbers: {result}")

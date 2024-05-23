#!/usr/bin/env python3
def print_fibonacci(length):
    if length <= 0:
        print("Enter a positive integer")
        return
    
    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])
    
    print(fib[:length])

# Example usage:
print_fibonacci(10)  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

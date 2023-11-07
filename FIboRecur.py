import timeit

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))

RUNS = 1000
fibonacci_sequence = fibonacci_recursive(n)


print("Fibonacci sequence (recursive):", fibonacci_sequence)
recursive_time = timeit.timeit(lambda: fibonacci_recursive(n), number=RUNS)
print("Total time taken (recursive):", recursive_time, "seconds")
print("Time Complexity: O(2^n)\n" "Space Complexity: O(n)\n")


import timeit

def fibonacci_non_recursive(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))

RUNS = 1000
fibonacci_sequence = fibonacci_non_recursive(n)


print("Fibonacci sequence (non-recursive):", fibonacci_sequence)
non_recursive_time = timeit.timeit(lambda: fibonacci_non_recursive(n), number=RUNS)
print("Total time taken (non-recursive):", non_recursive_time, "seconds")
print("Time Complexity: O(n)\n" "Space Complexity: O(1)\n")

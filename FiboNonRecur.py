import timeit

def fibonacci_non_recursive(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for i in range(n):
        fibonacci_sequence.append(a)
        c = a + b
        a = b
        b = c
    return fibonacci_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))

RUNS = 1000
fibonacci_sequence = fibonacci_non_recursive(n)


print("Fibonacci sequence (non-recursive):", fibonacci_sequence)
non_recursive_time = timeit.timeit(lambda: fibonacci_non_recursive(n), number=RUNS)
print("Total time taken (non-recursive):", non_recursive_time, "seconds")
print("Time Complexity: O(n)\n" "Space Complexity: O(1)\n")

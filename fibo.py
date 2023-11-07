# Recursive Fibonacci function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        # Recursively calculate Fibonacci numbers
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-Recursive Fibonacci function
def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)  # Print the first Fibonacci number
    if n > 1:
        print(second)  # Print the second Fibonacci number
    for _ in range(2, n):
        # Calculate the next Fibonacci number iteratively
        third = first + second
        first = second
        second = third
        print(third)

if __name__ == "_main_":
    n = int(input("Enter the number of Fibonacci numbers you want: "))
    for i in range(n):
        # Print Fibonacci numbers using the recursive function
        print(recursive_fibonacci(i))  # Recursive Fibonacci has exponential time and O(n) space complexity
    
    # Print Fibonacci numbers using the non-recursive function
    non_recursive_fibonacci(n)  # Non-recursive Fibonacci has linear (O(n)) time and constant (O(1)) space complexity
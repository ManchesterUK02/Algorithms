import timeit

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def main():
    weights = list(map(int, input("Enter the weights of items (separated by space): ").split()))
    values = list(map(int, input("Enter the values of items (separated by space): ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    max_value = knapsack_dynamic_programming(weights, values, capacity)
    RUNS = 1000
    
    print("Maximum value in the knapsack:", max_value)
    total_time = timeit.timeit(lambda: knapsack_dynamic_programming(weights, values, capacity), number=RUNS)
    print("Total time taken:", total_time, "seconds")

if __name__ == "__main__":
    main()

# weights = 3 4 6 5 
# values = 2 3 1 4
# capacity = 8

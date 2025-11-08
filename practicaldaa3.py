#Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], dp

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = []
    weights = []

    for i in range(n):
        val = int(input(f"Enter value of item {i + 1}: "))
        wt = int(input(f"Enter weight of item {i + 1}: "))
        values.append(val)
        weights.append(wt)

    capacity = int(input("Enter capacity of knapsack: "))

    max_value, dp_table = knapsack(values, weights, capacity)

    print("\nDynamic Programming Table:")
    for row in dp_table:
        print(row)

    print(f"\nMaximum value that can be obtained = {max_value}")

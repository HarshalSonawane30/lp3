# Write a program to solve a fractional Knapsack problem using a greedy method.
def fractional_knapsack(value, weight, capacity):
    n = len(value)
    ratio = []
    for i in range(n):
        ratio.append(value[i] / weight[i])
    items = list(zip(value, weight, ratio))
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity
    fractions = [0] * n

    print("\nItems (value, weight, ratio) sorted by ratio:")
    for val, wt, r in items:
        print(f"({val}, {wt}, {r:.2f})")

    for i in range(n):
        if items[i][1] <= remaining_capacity:
            total_value += items[i][0]
            remaining_capacity -= items[i][1]
            fractions[i] = 1
        else:
            fraction = remaining_capacity / items[i][1]
            total_value += items[i][0] * fraction
            fractions[i] = fraction
            break

    print(f"\nFractions of items taken: {fractions}")
    return total_value


if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    value = []
    weight = []

    for i in range(n):
        v = float(input(f"Enter value of item {i+1}: "))
        w = float(input(f"Enter weight of item {i+1}: "))
        value.append(v)
        weight.append(w)

    capacity = float(input("Enter capacity of knapsack: "))

    max_value = fractional_knapsack(value, weight, capacity)
    print(f"\nMaximum total value in knapsack = {max_value:.2f}")

# Write a program non-recursive and recursive program to calculate Fibonacci numbers and analyze their time and space complexity.

# Recursive Function
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# Non-Recursive (Iterative) Function
def fibonacci_iterative(n):
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b
# Main Program
def main():
    n = int(input("Enter the number of terms: "))

    print("\nFibonacci Series using Recursive Method:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\n\nFibonacci Series using Iterative Method:")
    for i in range(n):
        print(fibonacci_iterative(i), end=" ")

    print("\n")
if __name__ == "__main__":
    main()

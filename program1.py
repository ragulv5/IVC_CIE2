def sum_of_digits(N):
    N = abs(N)  # Handle negative numbers
    total = 0
    while N > 0:
        total += N % 10
        N //= 10
    return total

# User input
N = int(input("Enter an integer: "))
# Output the sum of digits
print("Sum of digits:", sum_of_digits(N))
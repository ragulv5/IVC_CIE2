def multiplication_table(N):
    for i in range(1, 11):
        print(f"{N} x {i} = {N * i}")

# User input
N = int(input("Enter an integer: "))
# Output the multiplication table
print("Multiplication table of", N, ":")
multiplication_table(N)

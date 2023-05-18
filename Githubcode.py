# Define the range for the multiplication table
start = 1
end = 12

# Generate and display the multiplication table
for i in range(start, end + 1):
    for j in range(start, end + 1):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()  # Print an empty line after each row of the table

# Create a list to store numbers
numbers = []

# Ask the user to enter 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Display numbers (first entry only for duplicates)
print("\nNumbers with no repeat entries are:")
displayed_numbers = []
  # List to track already displayed numbers

for num in numbers:
    if num not in displayed_numbers:
        displayed_numbers.append(num)
        print(num)


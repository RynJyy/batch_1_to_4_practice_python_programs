#Use for loop and range
odd_counter = 0
for i in range(10):
    #Ask 10 numbers
    num = int(input(f"Enter number {i+1}: "))
    #Count the number of odd numbers
    if num % 2 != 0:
        odd_counter += 1
#print the number of odd
print(f"\nThe number of odd numbers is {odd_counter}")
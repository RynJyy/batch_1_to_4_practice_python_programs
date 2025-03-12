#Use for loop and range
sum = 0
for i in range(10):
    #Ask user for a number
    num = int(input(f"Enter number {i + 1}: "))
    #Sum of the 10 num
    sum += num
#Print the sum
print(f"\nThe sum of the 10 numbers is {sum}")
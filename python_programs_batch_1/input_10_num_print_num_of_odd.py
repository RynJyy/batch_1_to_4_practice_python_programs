#Use for loop and range
result = 0
for i in range(10):
    #Ask 10 numbers
    num_of_odd = int(input(f"Enter number {i + 1}: "))
    #Count the number of odd numbers
    if num_of_odd % 2 != 0:
        result += 1
#Print result
print (f"\nThe number of odd numbers is {result}")
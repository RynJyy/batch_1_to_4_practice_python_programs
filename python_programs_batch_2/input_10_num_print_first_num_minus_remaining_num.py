#input num_1
num_1 = int(input("\nEnter the 1 number: "))
#use for loop and range for num_2 to num_10
for i in range(9):
    #Add the num_2 to num_10
    sum = int(input(f"Enter the {i+2} number: "))
#minus the sum to num_1
    num_1 -= sum
#print the result
print(f"\nThe result is {num_1}")
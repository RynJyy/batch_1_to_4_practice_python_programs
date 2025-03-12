#Ask 2 numbers
num_1 = int(input("\nEnter the first number: "))
num_2 = int(input("Enter the second number: "))
#Check the smaller number
if num_1 < num_2:
    #Print the smaller number
    print(f"\nThe smaller number is {num_1}")
elif num_2 < num_1:
    print(f"\nThe smaller number is {num_2}")
#if the input is equal
else:
    print("\nInvalid")
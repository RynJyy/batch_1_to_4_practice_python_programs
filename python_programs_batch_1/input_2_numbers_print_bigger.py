#Ask 2 numbers
num_1 = int(input("\nEnter the first number: "))
num_2 = int(input("Enter the second number: "))
#Check the bigger number
if num_1 > num_2:
    #Print the bigger number
    print(f"\nThe bigger number is: {num_1}")
elif num_2 > num_1:
    #Print the bigger number
    print(f"\nThe bigger number is: {num_2}")
else:
    #if bot numbers are equal
    print("\nInvalid")
#Ask 2 numbers
num_1 = int(input("\nEnter the first number: "))
num_2 = int(input("Enter the second number: "))
#Check if num 2 is not 0
if num_2 != 0:
    #Get the quotient
    quotient = num_1 / num_2
    #Print the quotient
    print(f"\nThe quotient of the numbers is {quotient:.2f}")
else:
    print("\nInvalid")
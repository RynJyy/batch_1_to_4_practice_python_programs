#Ask 2 numbers
num_01 = int(input("\nEnter the first number: "))
num_02 = int(input("Enter the second number: "))
#Check if num_02 is not equal to 0
if num_02 != 0:
    #Get the remainder
    remainder = num_01 % num_02
    #Print the remainder
    print(f"\nThe remainder is {remainder}")
#If num_02 is equal to 0
else:
    print("\nInvalid")
    
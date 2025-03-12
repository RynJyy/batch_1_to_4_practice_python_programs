#Ask 2 numbers
num_1 = int(input("\nEnter the first number: "))
num_2 = int(input("Enter the second number: "))
#Swap numbers if needed
if num_1 > num_2:
    num_1, num_2 = num_2, num_1
#Print numbers in between
for i in range(num_1+1, num_2):
    print(i)
#Check for no numbers in between
if num_1+1 == num_2 or num_1 == num_2:
    print("\nNo numbers in between")

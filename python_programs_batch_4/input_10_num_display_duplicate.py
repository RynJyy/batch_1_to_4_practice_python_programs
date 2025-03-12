#create a list
numbers = []
#use for loop and range to create a list of 10 numbers
for i in range (10):
    num = int(input(f"Enter a number: "))
    #append the list with the numbers 1 to 10
    numbers.append(num)
#check the duplicated numbers in the list
duplicates = []
for number in numbers:
    if numbers.count(number) > 1:
        duplicates.append(number)
#display the duplicated numbers
print(f"\nThe duplicated numbers are: {duplicates}")

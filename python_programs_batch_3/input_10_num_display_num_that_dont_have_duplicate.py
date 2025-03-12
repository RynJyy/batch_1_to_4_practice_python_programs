#Create a list
numbers = []
#Ask 10 numbers
for i in range(10):
    num = int(input(f"Enter the {i+1} number: "))
    numbers.append(num)
#Identify if numbers dont have duplicate
unique_numbers = 0
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers += 1
        #print the numbers that dont have duplicate
        print(f"\n The numbers that dont have duplicate:{num}")


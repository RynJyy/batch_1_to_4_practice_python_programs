# create a list to store numbers
numbers = []
# input 10 numbers
for i in range(10):
    num = int(input(f"Enter the {i+1} number: "))
    numbers.append(num)
# check if the number is not repeated
displayed_numbers = []
for num in numbers:
    if num not in displayed_numbers:
        displayed_numbers.append(num)
        # print the numbers make sure not to repeat the number
        print(num)



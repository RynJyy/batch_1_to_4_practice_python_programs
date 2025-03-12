#create list
numbers = []
#use while 
while True:
    #use try and except block
    try:
        num = int(input(f"Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
#get the average of the numbers
total = sum(numbers)
average = total / len(numbers)
#display the average
print(f"\nThe average of the numbers is: {average:.2f}")
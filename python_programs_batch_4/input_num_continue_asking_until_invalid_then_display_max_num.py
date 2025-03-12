#create list
numbers = []
#use while loop
while True:
    #use try and except block
    try:
        num = int(input(f"Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
#use max() function
if numbers:
    highest_num = max(numbers)
    #display the highest number
    print(f"\nThe highest number is: {highest_num}")
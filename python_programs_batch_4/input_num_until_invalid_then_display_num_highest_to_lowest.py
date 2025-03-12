#create list
numbers = []
#use while loop
while True:
    #use try and except
    try:
        num = int(input(f"Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
#use sort function to sort the list
numbers.sort(reverse = True)
#display the numbers in descending order
print(f"\nThe numbers in descending order are: {numbers}")
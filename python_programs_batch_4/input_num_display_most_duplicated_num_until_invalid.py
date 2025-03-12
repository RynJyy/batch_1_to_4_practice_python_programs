#create a list
numbers = []
#use while loop 
while True:
    try:
        num = int(input(f"Enter a number: "))
        #append the list with the numbers
        numbers.append(num)
    except ValueError:
        break
#check the duplicated numbers in the list
if numbers:
    most_duplicated = max(numbers, key = numbers.count)
    #display the most duplicated numbers
    print(f"\nThe most duplicated number is: {most_duplicated}")
else:
    print("No numbers entered.")

    


#create list to store numbers
numbers = []
#use while loop
while True:
    try:
        #input numbers
        num = int(input("Enter the number: "))
        numbers.append(num)
        #display the lowest number
        print(min(numbers))
    #continue until user input invalid number
    except ValueError:
        print("invalid")
        break

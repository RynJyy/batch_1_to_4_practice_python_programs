#create a list
numbers = []
#use while loop
while True:
    try:
        #input numbers
        num = int(input("Enter the number: "))
        numbers.append(num)
        #display lowest to highest
        numbers.sort()
        print(numbers)
    #continue until user input invalid number
    except ValueError:
        print("invalid")
        break    
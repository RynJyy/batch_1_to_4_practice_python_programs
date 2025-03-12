#create a list to store numbers
numbers = []
#use while loop
while True:
    try:
        #input numbers until 
        num = int(input("Enter the number: "))
        numbers.append(num)
        #if number is not repeated display unique
        if num is not numbers:
            print("unique")
        #if number is repeated display duplicate
        else:
            print("duplicate")
    #stop when user input invalid number
    except ValueError:
        print("invalid")
        break

    
    

        

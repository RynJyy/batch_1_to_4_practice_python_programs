#use for loops and range 
even_counter = 0
for i in range(10):
    num = int(input(f"Enter the {i+1} number: "))
    #identify the even numbers
    if num % 2 == 0:
        even_counter += 1
#print how many even numbers
print(f"\nThere are {even_counter} even numbers")

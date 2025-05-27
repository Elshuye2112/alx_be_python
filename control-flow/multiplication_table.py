# multiplication_table.py

# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table from 1 to 10
counter=0
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
    counter=counter+1

print(f" {counter} numbers has been multiplied with {number}")


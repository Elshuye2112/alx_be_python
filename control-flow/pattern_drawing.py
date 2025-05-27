# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    
    for col in range(size):
        print("*", end="")  
    print()  
    row += 1

print(f"There are {size} Columns and {row} Rows for the pattern")
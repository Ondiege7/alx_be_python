# 1. Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# 2. Initialize a row counter for the while loop
row = 0

# 3. Use a while loop to iterate through each row
while row < size:
    # 4. Use a nested for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    
    # 5. After the for loop finishes a row, print a newline character
    print()
    
    # 6. Increment the row counter to avoid an infinite loop
    row += 1
# 1. Prompt the user for a number
# We convert the input to an integer to perform multiplication
number = int(input("Enter a number to see its multiplication table: "))

# 2. Use a for loop to iterate from 1 to 10
# range(1, 11) starts at 1 and stops before 11 (so it hits 1 through 10)
for i in range(1, 11):
    # 3. Calculate the product
    product = number * i
    
    # 4. Print the result in the specific format: X * Y = Z
    print(f"{number} * {i} = {product}")
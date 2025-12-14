# 1. Prompt the user for their current age and store it.
# The input() function returns a string, so we wrap it in int() to convert it to a number.
current_age = int(input("How old are you? "))

# 2. Calculate the age in the future year (2050).
# Since the current year is assumed to be 2023, the difference is 27 years (2050 - 2023).
age_in_2050 = current_age + 27

# 3. Print the result in the specified format.
print(f"In 2050, you will be {age_in_2050} years old.")
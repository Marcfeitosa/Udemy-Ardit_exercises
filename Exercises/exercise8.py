import random

# Prompt the user to enter the first whole number
num1 = int(input("Enter the first whole number: "))

# Prompt the user to enter the second whole number
num2 = int(input("Enter the second whole number: "))

# Ensure num1 is smaller than num2
if num1 > num2:
    num1, num2 = num2, num1

# Generate a random number between num1 and num2 (inclusive)
random_number = random.randint(num1, num2)

# Print the generated random number
print(f"The random number between {num1} and {num2} is: {random_number}")
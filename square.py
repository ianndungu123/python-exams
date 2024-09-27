# Function to return the square of a number
def square_number(num):
    return num ** 2

# Taking input from the user
user_input = float(input("Enter a number: "))

# Calculating the square of the entered number
result = square_number(user_input)

# Displaying the result
print(f"The square of {user_input} is: {result}")

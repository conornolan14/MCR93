# We build a calculator that adds two numbers

# An input function will always return the input as a string
x = input('Enter the first number to be added: ')
y = input('Enter the second number to be added: ')
# We need to convert the strings into integer numbers
x = float(x)
y = float(y)
z = x + y
print('The sum of the two numbers is', z)

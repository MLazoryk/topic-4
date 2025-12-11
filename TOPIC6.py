# Define a function named 'say_hello' that takes one parameter called 'name'
# This function can be called later to print a greeting
def say_hello(name):
    # When called, this prints: "Hello, " followed by whatever name was provided
    # Example: say_hello('John') would print: "Hello, John"
    print(f'Hello, {name}')

# This print statement runs WHENEVER this file is loaded by Python
# It runs whether you run the file directly OR import it from another file
# The message is confusing because it says "imported" but that's not always true
print("You imported hello.py")

# This function call happens immediately when the file loads
# It calls the say_hello function with 'user' as the argument
# So "Hello, user" will always print when this file loads
say_hello('user')
"""
examples/basics.py
A simple script to demonstrate how to use the built-in `pdb` debugger.
You will learn how to:
  - Start pdb from the command line
  - Use `pdb.set_trace()` to inspect variables
  - Step through code interactively
"""

# This function adds two numbers and returns the result
def add_numbers(a, b):
    result = a + b  # Add the two input values
    return result   # Return the result to the caller

# This function multiplies two numbers and returns the result
def multiply_numbers(x, y):
    product = x * y  # Multiply the two input values
    return product   # Return the product to the caller

def main():
    a = 5  # Initialize variable a with value 5
    b = 10  # Initialize variable b with value 10
    sum_result = add_numbers(a, b)  # Call add_numbers() and store the result

    x = 3  # Initialize variable x with value 3
    y = 7  # Initialize variable y with value 7
    product_result = multiply_numbers(x, y)  # Call multiply_numbers() and store the result

    import pdb; pdb.set_trace()  # 🐞 Start the debugger at this point in the code

    # Output the sum result to the console
    print(f"Sum of {a} and {b} is {sum_result}")
    # Output the product result to the console
    print(f"Product of {x} and {y} is {product_result}")

# Entry point check: only run main() if this script is executed directly
if __name__ == "__main__":
    main()


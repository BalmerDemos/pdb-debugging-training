"""
examples/stepping_through.py
Demonstrates stepping through code line-by-line using `pdb`.
Use `n` (next), `s` (step into), and `r` (return) to follow program flow.
"""

def greet_user(name):
    message = f"Hello, {name}!"  # Create a greeting message
    return message  # Return the greeting

def main():
    user_name = "Alice"  # Define a user name
    import pdb; pdb.set_trace()  # Set a breakpoint here to start debugging

    greeting = greet_user(user_name)  # Call the greeting function
    print(greeting)  # Print the result

if __name__ == "__main__":
    main()
# This code sets up a simple program that can be debugged using pdb.
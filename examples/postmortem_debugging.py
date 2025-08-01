"""
examples/postmortem_debugging.py
Demonstrates postmortem debugging using pdb after an unhandled exception.
"""

def divide_numbers(a, b):
    return a / b  # This will crash if b is 0

def main():
    a = 10
    b = 0  # This will trigger a ZeroDivisionError
    result = divide_numbers(a, b)
    print(f"Result is: {result}")

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    import traceback # Module to print detailed exception traceback
    import pdb # Python debugger module

    try:
        main() # Attempt to run the main function
    except Exception:
        # Handle any exception that occurs during main()
        print("An exception occurred. Entering postmortem debugging...")
        traceback.print_exc() # Print the full traceback of the exception
        pdb.post_mortem()  # Launch debugger at the point where the exception occurred

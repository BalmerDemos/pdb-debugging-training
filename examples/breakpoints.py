"""
examples/breakpoints.py
This script demonstrates how to use `pdb.set_trace()` to pause execution,
inspect variables, and even modify them at runtime.
"""

def calculate_area(length, width):
    # Multiply length by width to get the area
    area = length * width
    # Return the computed area
    return area


def main():
    length = 8   # Length of the rectangle
    width = 5    # Width of the rectangle

    import pdb; pdb.set_trace()  # Manual breakpoint to inspect before calculation

    area = calculate_area(length, width)  # Compute area using the function
    print(f"The area of a {length}x{width} rectangle is {area}")

# Entry point check: only run main() if this script is executed directly
if __name__ == "__main__":
    main()

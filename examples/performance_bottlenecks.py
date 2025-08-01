"""
examples/performance_bottlenecks.py
Demonstrates how to identify performance bottlenecks using pdb and timing tools.
"""

import time  # Import the time module to measure execution time

def slow_function():
    total = 0
    for i in range(10_000_000):  # Simulate heavy computation using a loop
        total += i  # Accumulate the sum of numbers from 0 to 9,999,999
    return total  # Return the computed total


def fast_function():
    return sum(range(10_000_000))  # Optimized version using built-in sum function


def main():
    # Measure execution time for the slow function
    start = time.time()  # Record start time
    result = slow_function()  # Call the slow function
    end = time.time()  # Record end time

    # Print result and duration for the slow function
    print(f"Slow function result: {result}")
    print(f"Time taken (slow): {end - start:.4f} seconds")

    # Set a breakpoint for debugging and performance inspection
    import pdb; pdb.set_trace()  # Pause to inspect performance

    # Measure execution time for the fast function
    start = time.time()  # Record start time
    result = fast_function()  # Call the fast function
    end = time.time()  # Record end time

    # Print result and duration for the fast function
    print(f"Fast function result: {result}")
    print(f"Time taken (fast): {end - start:.4f} seconds")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
# This script demonstrates how to identify performance bottlenecks in Python code.
"""
examples/conditional_breakpoints.py
Demonstrates how to set conditional breakpoints in pdb.

Goal:
  - Pause only when a condition like i == 5 is True during iteration.
"""

def process_numbers():
    for i in range(1, 11):
        # Set a conditional breakpoint here:
        # break conditional_breakpoints.py:9 if i == 5
        print(f"Processing number: {i}")
        total = i * 2
        print(f"Double is: {total}")

if __name__ == "__main__":
    import pdb; pdb.set_trace()  # Start debugger before loop begins
    process_numbers()

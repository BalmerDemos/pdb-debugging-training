step-by-step walkthrough guide for using examples/conditional_breakpoints.py to teach or learn basic usage of the Python Debugger (pdb).

# pdb Walkthrough: examples/conditional_breakpoints.py
This guide will walk you through how to run the conditional_breakpoints.py file and use the pdb debugger step by step.

# 1. Activate Your Virtual Environment
Open your terminal and activate the virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

#  2. Navigate to Your Project Root
Make sure you're in the root of the project where examples/conditional_breakpoints.py is located.

cd pdb-debugging-training

#  3. Run the Script
Run the script normally — it will hit the pdb.set_trace() line and open the debugger:

python examples/conditional_breakpoints.py

You’ll see something like:

> .../examples/conditional_breakpoints.py(24)main()
-> print(f"Sum of {a} and {b} is {sum_result}")
(Pdb)
Now you're in the interactive pdb prompt!

# Step 1: Set a Conditional Breakpoint
Use s to step into the process_numbers() function:
(Pdb) s

Use n a few times to get into the loop, where i is defined:
(Pdb) n
(Pdb) n


# Step 2: Set a Conditional Breakpoint
Once you're inside the loop and i is defined, set a conditional breakpoint on the line that prints the current number:

(Pdb) break 13, i == 5

This tells pdb to break at line 13 only when i == 5.

# Step 3: Continue Execution
(Pdb) c

The program will run, and execution will pause when the condition is met:

Processing number: 1
Double is: 2
...
> conditional_breakpoints.py(13)process_numbers()
-> print(f"Processing number: {i}")
(Pdb)

# Step 4: Inspect Variables
Once the breakpoint hits:

(Pdb) p i
5

(Pdb) p total  # May not be available yet
(Pdb) n        # Execute current line
(Pdb) p total  # Now total is available

# Step 5: Resume Execution
(Pdb) c


# To see available lines and confirm the correct number, use:
(Pdb) l


Summary of Commands
| Command                | Description                  |
| ---------------------- | ---------------------------- |
| `s`                    | Step into function           |
| `n`                    | Next line                    |
| `break <line>, <cond>` | Set a conditional breakpoint |
| `p var`                | Print a variable’s value     |
| `c`                    | Continue execution           |
| `q`                    | Quit the debugger            |

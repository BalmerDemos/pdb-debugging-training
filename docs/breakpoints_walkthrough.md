# pdb Walkthrough: examples/breakpoints.py
This guide will walk you through how to run the breakpoints.py file and use the pdb debugger step by step.

# 1. Activate Your Virtual Environment
Open your terminal and activate the virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

#  2. Navigate to Your Project Root
Make sure you're in the root of the project where examples/breakpoints.py is located.

cd pdb-debugging-training

#  3. Run the Script
Run the script normally — it will hit the pdb.set_trace() line and open the debugger:

python examples/breakpoints.py

You’ll see something like:

> .../examples/breakpoints.py(14)main()
-> area = calculate_area(length, width)
(Pdb)

Now you're in the interactive pdb prompt!

# Step-by-Step Debugging

# Step 1: Inspect Variables
(Pdb) p length
8

(Pdb) p width
5
p calculate_area(length, width)
40

# Step 2: Modify Variables (Optional)
(Pdb) length = 10
(Pdb) width = 10
(Pdb) p calculate_area(length, width)

You just changed the rectangle size during runtime.

# Step 3: Continue Execution
(Pdb) c

Now the program finishes and prints the result using your modified values.

# Summary of Commands

| Command       | Description                      |
| ------------- | -------------------------------- |
| `p var`       | Print variable value             |
| `length = 10` | Change variable during execution |
| `l`           | List surrounding code            |
| `n`           | Step to next line                |
| `c`           | Continue execution               |
| `q`           | Quit debugger                    |

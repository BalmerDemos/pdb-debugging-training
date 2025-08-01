step-by-step walkthrough guide for using examples/stepping_through.py to teach or learn basic usage of the Python Debugger (pdb).

# pdb Walkthrough: examples/stepping_through.py
This guide will walk you through how to run the stepping_through.py file and use the pdb debugger step by step.

# 1. Activate Your Virtual Environment
Open your terminal and activate the virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

#  2. Navigate to Your Project Root
Make sure you're in the root of the project where examples/stepping_through.py is located.

cd pdb-debugging-training

#  3. Run the Script
python examples/stepping_through.py
(Pdb)

Now you're in the interactive pdb prompt!

# Step-by-Step Debugging

Step 1: Inspect Variables
(Pdb) p user_name
'Alice'


Step 2: Step Over a Line
(Pdb) n

This executes the current line and moves to the next. Try this until you're on the greet_user() line.

Step 3: Step Into a Function
(Pdb) s

This steps into the greet_user() function so you can see it execute line by line.

Step 4: Step Out of the Function
(Pdb) r

This tells pdb to run until the current function returns.

Step 5: Continue Execution
(Pdb) c

This resumes the program until the end.





# basics walkthrough
step-by-step walkthrough guide for using examples/basics.py to teach or learn basic usage of the Python Debugger (pdb).

# pdb Walkthrough: examples/basics.py
This guide will walk you through how to run the basics.py file and use the pdb debugger step by step.

# 1. Activate Your Virtual Environment
Open your terminal and activate the virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

#  2. Navigate to Your Project Root
Make sure you're in the root of the project where examples/basics.py is located.

cd pdb-debugging-training

#  3. Run the Script
Run the script normally — it will hit the pdb.set_trace() line and open the debugger:

python examples/basics.py
You’ll see something like:

> .../examples/basics.py(24)main()
-> print(f"Sum of {a} and {b} is {sum_result}")
(Pdb)
Now you're in the interactive pdb prompt!

🧪 Step-by-Step Guide
Here’s how to explore the code using pdb:

# Step 1: List the Code

(Pdb) l
This lists the surrounding source code.

# Step 2: Print Variable Values

(Pdb) p a
5

(Pdb) p b
10

(Pdb) p sum_result
15

(Pdb) p product_result
21
This shows you the values of variables at this point in the code.

# Step 3: Step to the Next Line

(Pdb) n
This executes the current line (print(f"Sum of...) and moves to the next line.

# Step 4: Step Into a Function (if applicable)
You can go inside function calls using:


(Pdb) s
But in this case, the function calls are done already — use s if you're paused before a function call.

# Step 5: Continue Execution
Once you're done inspecting:


(Pdb) c
This resumes normal script execution.

# Step 6: Quit at Any Time

(Pdb) q
This exits the debugger immediately.
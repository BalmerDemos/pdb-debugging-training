step-by-step walkthrough guide for using examples/postmortem_debugging.py to teach or learn basic usage of the Python Debugger (pdb).

# pdb Walkthrough: examples/postmortem_debugging.py
This guide will walk you through how to run the postmortem_debugging.py file and use the pdb debugger step by step.

# 1. Activate Your Virtual Environment
Open your terminal and activate the virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

#  2. Navigate to Your Project Root
Make sure you're in the root of the project where examples/postmortem_debugging.py is located.

cd pdb-debugging-training

#  3. Run the Script
The script will raise a ZeroDivisionError, print a traceback, and drop you into pdb automatically via pdb.post_mortem().

#  What You’ll See
An exception occurred. Entering postmortem debugging...
Traceback (most recent call last):
  File "examples/postmortem_debugging.py", line 19, in <module>
    main()
  File "examples/postmortem_debugging.py", line 11, in main
    result = divide_numbers(a, b)
  File "examples/postmortem_debugging.py", line 7, in divide_numbers
    return a / b
ZeroDivisionError: division by zero
> examples/postmortem_debugging.py(7)divide_numbers()
-> return a / b
(Pdb)


#  Step-by-Step Debugging

#  Step 1: Inspect Variables

(Pdb) p a
10

(Pdb) p b
0


#  Step 2: Navigate the Call Stack

(Pdb) bt       # Show full traceback
(Pdb) up       # Move up to the caller frame
(Pdb) down     # Move back down


#  Step 3: List Source Code
(Pdb) l

#  Summary of Commands

| Command | Description              |
| ------- | ------------------------ |
| `p var` | Print a variable value   |
| `l`     | List source code         |
| `bt`    | Show full traceback      |
| `up`    | Move up the call stack   |
| `down`  | Move down the call stack |
| `q`     | Quit the debugger        |

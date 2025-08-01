step-by-step walkthrough guide for using examples/performance_bottlenecks.py to teach or learn basic usage of the Python Debugger (pdb).

# pdb Walkthrough: examples/performance_bottlenecks.py
This guide will walk you through how to run the performance_bottlenecks.py file and use the pdb debugger step by step.

# 1. Activate Your Virtual Environment
Open your terminal and activate the virtual environment:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 2. Navigate to Your Project Root
Make sure you're in the root of the project where examples/performance_bottlenecks.py is located.

cd pdb-debugging-training

# 3. Run the Script
python examples/performance_bottlenecks.py

You'll see output for the slow function, followed by a pause at pdb.set_trace().

# What You’ll See

Slow function result: 49999995000000
Time taken (slow): <about 0.4+ seconds>
> examples/performance_bottlenecks.py(23)main()
-> start = time.time()
(Pdb)

# Step-by-Step Debugging

# Step 1: Compare Function Execution

(Pdb) p slow_function
(Pdb) p fast_function

You can also time each one again inside the debugger if needed.

# Step 2: Inspect Performance Difference

Step forward to run the fast version:

(Pdb) n
(Pdb) n
...

Observe the second block executes much faster.

# Step 3: Re-run Timing from Debugger (optional)

(Pdb) import time
(Pdb) t0 = time.time()
(Pdb) fast_function()
(Pdb) time.time() - t0

# Summary of Commands

| Command       | Description              |
| ------------- | ------------------------ |
| `p func()`    | Print result of function |
| `n`           | Next line                |
| `c`           | Continue execution       |
| `import time` | Import for inline timing |
| `q`           | Quit debugger            |

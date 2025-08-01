
# pdb Debugging Tips

Use these tips to debug smarter, not harder, when working with pdb.

# 1. Start with pdb.set_trace() or breakpoint()
Insert a breakpoint where things start going wrong:

import pdb; pdb.set_trace()
# or in Python 3.7+
breakpoint()

Use this to pause execution and start inspecting.

# 2. Inspect Variables Right Away

Use p var_name to print the value of any variable at the current line:

(Pdb) p user_input
(Pdb) p len(data)

Use this before and after changes to compare.

# 3. Use n, s, and r Wisely

n – Step over the current line

s – Step into a function call

r – Step out of the current function

Step through line by line to find exactly when things break.


# 4. Use Conditional Breakpoints
Set a breakpoint only when a certain condition is met:

(Pdb) break 25, counter > 100
Helps you skip repetitive steps and pause only when necessary.

# 5. Measure Performance in the Debugger
You can do inline performance timing in the prompt:
(Pdb) import time
(Pdb) t0 = time.time()
(Pdb) slow_function()
(Pdb) time.time() - t0

Great for comparing function performance on the fly.

# 7. Keep Your Debugging Clean
Remove or comment out pdb.set_trace() before committing code

Avoid printing too much — it clutters the prompt

Use short variable names for experiments in the debugger

# BONUS: Practice Often
Like learning a musical instrument, becoming great at debugging takes repetition. Run small scripts and intentionally break them to build muscle memory using pdb.
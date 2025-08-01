
# Python Debugger (pdb) Command Reference

https://docs.python.org/3/library/pdb.html


# Stepping Through Code

| Command | Description                                             |
| ------- | ------------------------------------------------------- |
| `n`     | Next: execute the current line and move on              |
| `s`     | Step into: go into function calls                       |
| `r`     | Return: continue until the current function returns     |
| `c`     | Continue: resume execution until next breakpoint or end |
| `q`     | Quit: exit the debugger                                 |

# Breakpoints

| Command                       | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| `break <lineno>`              | Set a breakpoint at a specific line              |
| `break <file>:<lineno>`       | Set a breakpoint in another file                 |
| `break`                       | List all breakpoints                             |
| `disable <bpnum>`             | Disable a breakpoint                             |
| `enable <bpnum>`              | Enable a breakpoint                              |
| `clear <bpnum>`               | Remove a breakpoint                              |
| `break <lineno>, <condition>` | Set a **conditional** breakpoint (e.g. `i == 5`) |


# Code Context
| Command | Description                                     |
| ------- | ----------------------------------------------- |
| `l`     | List source code near the current line          |
| `ll`    | List the entire function’s source code          |
| `a`     | Print the argument list of the current function |
| `w`     | Print where you are in the code                 |


# Timing and Experimentation (Advanced Use)
| Command            | Description                               |
| ------------------ | ----------------------------------------- |
| `import time`      | Import time module manually in debugger   |
| `t0 = time.time()` | Start timing manually                     |
| `time.time() - t0` | Get elapsed time after function execution |


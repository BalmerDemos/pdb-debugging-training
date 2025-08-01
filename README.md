# pdb-debugging-training-
A hands-on Python repository for learning and teaching debugging and performance optimization using pdb, ipdb, and profiling tools.

# Project Overview
This project is designed for developers, students, or teams who want to improve their debugging skills in Python using:

- The built-in Python Debugger (pdb)

- Advanced tools like ipdb, line_profiler, and memory_profiler

- Realistic and focused code examples

# Setup Instructions

# 1. Clone the Repository
git clone https://github.com/your-username/pdb-debugging-training.git
cd pdb-debugging-training


## Setting Up the Virtual Environment

# Create a virtual environment

# Activate it
# On Linux/macOS:
python3 -m venv venv
source venv/bin/activate


# On Windows:
python -m venv venv
venv\Scripts\activate
or
python3 -m venv venv

# Install desired packages:
pip install ipdb line_profiler memory_profiler pytest

# Install dependencies
pip install -r requirements.txt

# This will write all currently installed packages
pip freeze > requirements.txt

# Project Structure

examples/
├── basics.py                   # Intro to pdb
├── breakpoints.py              # Manual and conditional breakpoints
├── conditional_breakpoints.py # Breakpoints triggered by conditions
├── performance_bottlenecks.py # Timing and profiling code
├── postmortem_debugging.py    # pdb.post_mortem() in exception handling
├── stepping_through.py        # Using n/s/r to walk through execution
docs/
├── walkthrough files          # Step-by-step guides for each example


# Running the Examples
Each file in the examples/ directory is self-contained and demonstrates a core debugging concept.

Example:

python examples/breakpoints.py

Then follow the printed instructions or refer to the walkthrough in docs/walkthroughs files/.

# Useful pdb Commands

| Command | Description                 |
| ------- | --------------------------- |
| `p var` | Print variable              |
| `n`     | Next line                   |
| `s`     | Step into function          |
| `r`     | Return from function        |
| `c`     | Continue execution          |
| `l`     | List code                   |
| `bt`    | Backtrace (show call stack) |
| `break` | Set a breakpoint            |
| `q`     | Quit debugger               |


# Contributions
Feel free to open issues or submit PRs to add more examples, walkthroughs, or tooling tips!



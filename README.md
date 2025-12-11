# Page-Handling-Sim
## Overview

This project is a simple educational simulator that demonstrates how the FIFO (First-In, First-Out) Page Replacement Algorithm works in virtual memory management.
Users can enter a reference string and number of frames, and the simulator will display step-by-step how pages are loaded, replaced, and managed inside memory frames.

This project includes both:
- A console-based FIFO simulation, and
- A Tkinter GUI application for interactive use.
## Features

- Accepts a reference string (max 10 pages).
- Allows selection of **3–5 memory frames.**
- Simulates FIFO page replacement.
- Displays:
  - Current frame contents
  - Hits and page faults
  - Replaced pages (if any)
  - Total number of page faults
- Simple and user-friendly Tkinter graphical interface.
## How to Run the Program
1. Requirements
- Python 3.x
- Tkinter
2. Running the GUI
Run the main Python file:

```bash
python fifoSim.py
```
## Input Format

Reference string:
A sequence of integers separated by spaces
Example:
```
7 0 1 2 0 3 0 4
```
Number of frames:
Integer between 3 and 5

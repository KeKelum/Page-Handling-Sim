import tkinter as tk
from tkinter import ttk, messagebox


# Validation function
''' Ensures that user input values are validated before running the simulation '''
# ---------------------------------------------------------
def validate_inputs(ref_str, frames_count):
    if len(ref_str) == 0 or len(ref_str) > 10:
        raise ValueError("Reference string must contain 1 to 10 pages.")
    if not (3 <= frames_count <= 5):
        raise ValueError("Number of frames must be between 3 and 5.")



# FIFO Simulation
''' Simulate FIFO page replacement algorithm '''
# ---------------------------------------------------------
def simulate_fifo(reference_string, frames_count):
    validate_inputs(reference_string, frames_count)

    frames = []
    next_to_replace = 0
    page_faults = 0
    output = []

    output.append("-" * 60)
    output.append(f"FIFO Simulation — frames: {frames_count}, references: {reference_string}")
    output.append("-" * 60)

    for step, page in enumerate(reference_string, start=1):
        before = frames.copy()

        if page in frames:
            event = "Hit"
        else:
            page_faults += 1
            event = "Page Fault"

            if len(frames) < frames_count:
                frames.append(page)
                event += " (loaded into free frame)"
            else:
                replaced = frames[next_to_replace]
                frames[next_to_replace] = page
                event += f" (replaced page {replaced})"
                next_to_replace = (next_to_replace + 1) % frames_count

        output.append(f"Step {step:2d}: Ref = {page:2d} | Before: {before} | {event}")
        output.append(f"          After : {frames}")
        output.append("-" * 60)

    output.append(f"Total page faults: {page_faults}")
    return "\n".join(output)



# 
''' 
 Connect simulate_fifo() to the GUI
 Runs the simulation
 Read GUI input
 Display Output '''
# ---------------------------------------------------------
def run_simulation():
    ref_str_raw = entry_ref.get().strip()
    frames_raw = entry_frames.get().strip()

    try:
        ref_list = list(map(int, ref_str_raw.split()))
        frames_count = int(frames_raw)
    except:
        messagebox.showerror("Input Error", "Invalid number format.")
        return

    try:
        result = simulate_fifo(ref_list, frames_count)

        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, result)
        text_output.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))



# BUILD GUI
'''
Input area for page reference 
Input area for frame count
Button for run simulation
Output area for display final output '''
# ---------------------------------------------------------
root = tk.Tk()
root.title("FIFO Page Replacement Simulator")
root.geometry("720x520")

# Input frame
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Input area for reference string
tk.Label(frame_input, text="Reference String (space-separated):").grid(row=0, column=0, sticky="w")
entry_ref = tk.Entry(frame_input, width=40)
entry_ref.grid(row=0, column=1, padx=10)

# Input area for frame counts
tk.Label(frame_input, text="Number of Frames (3-5):").grid(row=1, column=0, sticky="w")
entry_frames = tk.Entry(frame_input, width=10)
entry_frames.grid(row=1, column=1, sticky="w")

# Button for run simulation 
btn_run = tk.Button(root, text="Simulate", width=20, command=run_simulation)
btn_run.pack(pady=10)

# Output box with a scrollbar
frame_output = tk.Frame(root)
frame_output.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_output)
scrollbar.pack(side="right", fill="y")

text_output = tk.Text(frame_output, wrap="none", yscrollcommand=scrollbar.set, state="disabled")
text_output.pack(fill="both", expand=True)

scrollbar.config(command=text_output.yview)

root.mainloop()

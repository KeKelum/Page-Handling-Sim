import tkinter as tk
from tkinter import ttk, messagebox

def validate_inputs(ref_str, frames_count):
    if len(ref_str) == 0 or len(ref_str) > 10:
        raise ValueError("Reference string must contain 1 to 10 pages.")
    if not (3 <= frames_count <= 5):
        raise ValueError("Number of frames must be between 3 and 5.")
    return True

def simulate_fifo(reference_string, frames_count):
    validate_inputs(reference_string, frames_count)

    frames = []
    next_to_replace = 0   # index in frames list
    page_faults = 0

    print("-" * 60)
    print(f"FIFO Simulation — frames: {frames_count}, references: {reference_string}")
    print("-" * 60)

    for step, page in enumerate(reference_string, start=1):
        before = frames.copy()
        event = ""
        replaced = None

        if page in frames:
            # Hit
            event = "Hit"
        else:
            # Page Fault
            page_faults += 1
            event = "Page Fault"

            if len(frames) < frames_count:
                # Free frame exists — just add
                frames.append(page)
                event += " (loaded into free frame)"
            else:
                # Replace using FIFO
                replaced = frames[next_to_replace]
                frames[next_to_replace] = page
                event += f" (replaced page {replaced})"
                next_to_replace = (next_to_replace + 1) % frames_count

        print(f"Step {step:2d}: Ref page = {page:2d} | Frames before: {before} | {event}")
        print(f"          Frames after : {frames}")
        print("-" * 60)

    print(f"Total page faults: {page_faults}")
    return page_faults


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


root = tk.Tk()
root.title("FIFO Page Replacement Simulator")
root.geometry("720x520")

# Input frame
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Reference String (space-separated):").grid(row=0, column=0, sticky="w")
entry_ref = tk.Entry(frame_input, width=40)
entry_ref.grid(row=0, column=1, padx=10)

tk.Label(frame_input, text="Number of Frames (3-5):").grid(row=1, column=0, sticky="w")
entry_frames = tk.Entry(frame_input, width=10)
entry_frames.grid(row=1, column=1, sticky="w")

btn_run = tk.Button(root, text="Simulate", width=20, command=run_simulation)
btn_run.pack(pady=10)

# Output box with scrollbar
frame_output = tk.Frame(root)
frame_output.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_output)
scrollbar.pack(side="right", fill="y")

text_output = tk.Text(frame_output, wrap="none", yscrollcommand=scrollbar.set, state="disabled")
text_output.pack(fill="both", expand=True)

scrollbar.config(command=text_output.yview)

root.mainloop()

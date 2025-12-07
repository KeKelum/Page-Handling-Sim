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


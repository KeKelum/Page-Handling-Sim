def validate_inputs(ref_str, frames_count):
    if len(ref_str) == 0 or len(ref_str) > 10:
        raise ValueError("Reference string must contain 1 to 10 pages.")
    if not (3 <= frames_count <= 5):
        raise ValueError("Number of frames must be between 3 and 5.")
    return True

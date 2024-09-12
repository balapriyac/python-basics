from functools import partial

def format_text(text, alignment="left", width=80):
    if alignment == "center":
        return text.center(width)
    elif alignment == "right":
        return text.rjust(width)
    else:
        return text.ljust(width)

# Create a partial function for center alignment with a specific width
centered_text = partial(format_text, alignment="center", width=50)

# Use the partial function without passing alignment or width
print(centered_text("Partial Functions")) 

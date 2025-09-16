def load_csv(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]
    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]
    return header, rows

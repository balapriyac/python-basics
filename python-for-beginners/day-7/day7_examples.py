def load_csv(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]
    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]
    return header, rows

def detect_type(value):
    try:
        float(value)
        return "numeric"
    except:
        return "text"

def profile_columns(header, rows):
    summary = {}
    for i, col in enumerate(header):
        values = [row[i].strip() for row in rows if len(row) == len(header)]
        col_type = detect_type(values[0])
        unique = set(values)
        summary[col] = {
            "type": col_type,
            "unique_count": len(unique),
            "most_common": max(set(values), key=values.count)
 }
 if col_type == "numeric":
 nums = [float(v) for v in values if v.replace('.', '', 1).isdigit()]
 summary[col]["average"] = sum(nums) / len(nums) if nums else 0
 return summary

def write_summary(summary, out_file):
    with open(out_file, "w") as f:
        for col, stats in summary.items():
            f.write(f"Column: {col}\n")
            for k, v in stats.items():
                f.write(f"  {k}: {v}\n")
            f.write("\n")

header, rows = load_csv("employees.csv")
summary = profile_columns(header, rows)
write_summary(summary, "profile_report.txt")


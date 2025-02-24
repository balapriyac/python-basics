from functools import singledispatch
from datetime import date, datetime

@singledispatch
def format_output(obj):
    return str(obj)

@format_output.register
def _(obj: int):
    return f"INTEGER: {obj:+d}"

@format_output.register
def _(obj: float):
    return f"FLOAT: {obj:.2f}"

@format_output.register
def _(obj: date):
    return f"DATE: {obj.strftime('%Y-%m-%d')}"

@format_output.register(list)
def _(obj):
    return f"LIST: {', '.join(format_output(x) for x in obj)}"

# Usage
results = [
    format_output("Hello"),
    format_output(42),
    format_output(-3.14159),
    format_output(date(2025, 2, 21)),
    format_output([1, 2.5, "three"])
]

for r in results:
    print(r)

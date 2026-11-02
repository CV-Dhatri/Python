"""
hospital/display.py
Console formatting helpers using tabulate-style table printing.
"""

def print_header(title: str):
    """Prints a styled section header."""
    width = 60
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)

def print_table(headers: list, rows: list):
    """
    Renders rows into a clean, aligned console table.
    """
    if not rows:
        print("\n[!] No records found.\n")
        return

    str_rows = [[str(item) if item is not None else "NULL" for item in row] for row in rows]
    
    col_widths = [len(h) for h in headers]
    for row in str_rows:
        for idx, val in enumerate(row):
            if len(val) > col_widths[idx]:
                col_widths[idx] = len(val)

    sep_line = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    header_line = "| " + " | ".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers)) + " |"

    print("\n" + sep_line)
    print(header_line)
    print(sep_line)
    for row in str_rows:
        row_line = "| " + " | ".join(f"{val:<{col_widths[i]}}" for i, val in enumerate(row)) + " |"
        print(row_line)
    print(sep_line + "\n")
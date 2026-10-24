
"""
RECORD CHECK - my version
===========================

Name  : Elisee Mukunzi
Lane  : IT
Date  : 2026/10/24

Run it: python template.py
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Calculate the difference, percentage and status of a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if value >= limit:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print(f"Record: {label}")
    print(f"Value: {value:.2f}")
    print(f"Limit: {limit:.2f}")
    print(f"Difference: {difference:.2f}")
    print(f"Percentage: {percent:.1f}%")
    print(f"Status: {status}")
    print("-" * 30)


# ====================================================================== STORE

def load_records(path):
    """Load records from a file into a list of dictionaries."""
    records = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if line:
                label, value, limit = line.split(",")

                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })

    return records


# Create your own data file: records.txt
try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("Error: records.txt was not found.")
    records = []


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0

try:
    with open("results.txt", "w") as results_file:
        for record in records:
            difference, percent, status = check_record(
                record["value"],
                record["limit"]
            )

            print_report(
                record["label"],
                record["value"],
                record["limit"],
                difference,
                percent,
                status
            )

            if status == "OVER LIMIT":
                over_limit_count += 1

            results_file.write(
                f"{record['label']}, {status}\n"
            )

    print(f"Summary: {over_limit_count} of {len(records)} were OVER LIMIT.")

except OSError as e:
    print(f"Error writing results: {e}")


"""
RECORD CHECK - my version

Name  :Elisee Mukunzi
Lane  : IT
Date  :2026/10/24
"""


# ======================================================================
# 1. CLASS

class Record:
    """Store record details and check their status."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialize a record with its label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage of the limit."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ======================================================================
# 2. LOAD RECORDS FROM A FILE

def load_records(path):
    """Load records from a file and return a list of Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records


# ======================================================================
# CREATE THE DATA FILE

with open("records.txt", "w") as file:
    file.write("R-001,87,100\n")
    file.write("R-002,95,100\n")
    file.write("R-003,120,100\n")
    file.write("R-004,45,100\n")


records = load_records("records.txt")


# ======================================================================
# 3. PRINT THE REPORT

over_limit_count = 0

for record in records:
    result = record.status()

    if result == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"  Label  : {record.label}")
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {result}")
    print("=" * 34)

print()
print(f"Total records over limit: {over_limit_count}")


"""
RECORD CHECK - my version
===========================

Name  : Elisee
Lane  : IT
Date  : 2026/10/24
"""


# =================================================================== FUNCTIONS

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the complete record check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


# ==================================================================== INPUT

over_limit_count = 0

while True:
    label = input("Enter hostname (or quit to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter total GB: "))


    # ================================================================= PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1


    # ================================================================= OUTPUT

    print_report(label, value, limit, difference, percent, status)


# ==================================================================== SUMMARY

print()
print("=" * 34)
print(f"Records OVER LIMIT: {over_limit_count}")
print("=" * 34)

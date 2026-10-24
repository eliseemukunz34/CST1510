
"""
RECORD CHECK - my version
===========================

Name  : Elisee
Lane  : IT
Date  : 2026/10/24

Run it: python template.py
"""

# ==================================================================== INPUT
# 1. Ask the user for three values.

label = input("Enter a name, hostname, or IP: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))


# ================================================================== PROCESS
# 2. Calculate the difference and percentage.

difference = first - second
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)

print(f"First value:       {first:>10.2f}")
print(f"Second value:      {second:>10.2f}")
print(f"Difference:        {difference:>+10.2f}")
print(f"Percentage:        {percent:>10.2f}%")

print("Check completed successfully.")

print("=" * 34)

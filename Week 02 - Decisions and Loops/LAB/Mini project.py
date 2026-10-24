
"""
RECORD CHECK - my version
===========================

Name  : Elisee
Lane  : IT
Date  : 2026/10/24

Run it: python template.py
"""

# INPUT

label = input("Label: ")
value = float(input("Value: "))
limit = float(input("Limit: "))

# PROCESS

difference = limit - value
percent = value / limit * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)

print(f"Value      : {value:10.2f}")
print(f"Limit      : {limit:10.2f}")
print(f"Difference : {difference:10.2f}")
print(f"Percent    : {percent:10.2f} %")
print(f"Status     : {status:>10}")

print("=" * 34)


"""
RECORD CHECK - my version

Name  : Elisee Mukunzi
Lane  : IT
Date  : 24/10/2026
"""

# ====================================================================
# 1. INPUT

label = input("Enter hostname: ")
first = float(input("Enter GB used: "))
second = float(input("Enter total GB: "))


# ====================================================================
# 2. PROCESS

difference = second - first
percent = (first / second) * 100
free_percent = (difference / second) * 100


# ====================================================================
# 3. OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)

print(f"  Hostname       : {label}")
print(f"  GB used        : {first:>10.2f}")
print(f"  GB total       : {second:>10.2f}")
print(f"  GB remaining   : {difference:>+10.2f}")
print(f"  Storage used   : {percent:>9.2f}%")
print(f"  Storage free   : {free_percent:>9.2f}%")

# Storage free helps an IT administrator see how much capacity
# is still available on the server.

print("=" * 34)

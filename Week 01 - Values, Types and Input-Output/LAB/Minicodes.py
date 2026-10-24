
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


# ====================================================================
# 3. OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)

print(f"  Hostname       : {label}")
print(f"  GB used        : {first:>+10.2f}")
print(f"  GB total       : {second:>10.2f}")
print(f"  GB remaining   : {difference:>+10.2f}")
print(f"  Storage used   : {percent:>9.2f}%")
print(f"  Storage status : {'FULL' if percent >= 100 else 'OK'}")

print("=" * 34)

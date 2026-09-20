# Day 8 - Core Data Structures
# Count numbers that have even digits

# Simulated user data
numbers = [12, 345, 6789, 2468, 135, 42, 9876, 111, 200]

count = 0

print("User Data:", numbers)
print("\nNumbers with even digits:")

for number in numbers:
    # Count digits
    digit_count = len(str(abs(number)))

    if digit_count % 2 == 0:
        print(number)
        count += 1

print("\nTotal numbers with even digits:", count)
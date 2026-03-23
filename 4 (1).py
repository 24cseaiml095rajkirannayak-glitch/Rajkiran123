students = {}

# Add entries
students["Rahul"] = 85
students["Aman"] = 90
students["Neha"] = 78

# Update
students["Rahul"] = 88

# Delete
del students["Neha"]

print("Dictionary:", students)
print("Keys:", list(students.keys()))
print("Values:", list(students.values()))
print("Items:", list(students.items()))

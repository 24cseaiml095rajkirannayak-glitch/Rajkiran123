students = {}

def add_student(name, roll, marks):
    students[roll] = {"name": name, "marks": marks}

def update_marks(roll, new_marks):
    if roll in students:
        students[roll]["marks"] = new_marks

def compute_average(roll):
    if roll in students:
        m = students[roll]["marks"]
        return sum(m) / len(m)
    return None

def find_topper():
    topper_roll = None
    topper_avg = -1
    for roll, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        if avg > topper_avg:
            topper_avg = avg
            topper_roll = roll
    return topper_roll, topper_avg

add_student("Rahul", 1, [80, 90, 85])
add_student("Aman", 2, [88, 92, 81])
add_student("Neha", 3, [70, 75, 80])

update_marks(3, [78, 82, 79])

print("Students:", students)
print("Average of roll 1:", compute_average(1))
print("Topper (roll, avg):", find_topper())

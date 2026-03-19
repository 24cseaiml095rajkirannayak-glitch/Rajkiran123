

rooms = {} 

print("Room Allotment System")
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i+1)
    name = input("Enter student name: ")
    year = input("Enter year (1 to 4): ")
    count=0

    if year == "1":
        room = "Room 101"
        count=count+1
    elif year == "2":
        room = "Room 102"
        count=count+1
    elif year == "3":
        room = "Room 103"
        count=count+1
    elif year == "4":
        room = "Room 104"
    else:
        room = "Invalid year"

    rooms[name] = room

print("\n--- Final Room Allotment ---")
for student in rooms:
    print(student, "→", rooms[student])
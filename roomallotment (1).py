def allocate_room(student_name, room_type, duration):
    if room_type == "Single":
        cost = 1000
    elif room_type == "Double":
        cost = 1500
    elif room_type == "Suite":
        cost = 2500
    else:
        return "Invalid room type"

    total_cost = cost * duration
    return f"{student_name} has been allocated a {room_type} room for {duration} months. Total cost: ${total_cost}"
print("Welcome to the Room Allotment System")
student_name = input("Enter student name: ")
room_type = input("Enter room type (Single/Double/Suite): ")
duration = int(input("Enter duration of stay in months: "))
result = allocate_room(student_name, room_type, duration)
print(result)
         
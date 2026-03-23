employees = {}

while True:
    print("\n1. Add employee")
    print("2. Remove employee")
    print("3. Display employees")
    print("4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter employee name: ")
        employees[name] = "Present"
    elif ch == "2":
        name = input("Enter employee name to remove: ")
        if name in employees:
            del employees[name]
            print("Removed.")
        else:
            print("Employee not found.")
    elif ch == "3":
        if not employees:
            print("No employees.")
        else:
            for name, status in employees.items():
                print(name, "-", status)
    elif ch == "4":
        break
    else:
        print("Invalid choice.")

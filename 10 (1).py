students = []

while True:
    print("\n1. Add student record")
    print("2. Show all")
    print("3. Show passed")
    print("4. Show failed")
    print("5. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Name: ")
        roll = input("Roll: ")
        marks = float(input("Marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})
    elif ch == "2":
        for s in students:
            print(s)
    elif ch == "3":
        for s in students:
            if s["marks"] >= 40:
                print(s)
    elif ch == "4":
        for s in students:
            if s["marks"] < 40:
                print(s)
    elif ch == "5":
        break
    else:
        print("Invalid choice.")

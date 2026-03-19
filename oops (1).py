#parking-lot
# class ParkingLot:
#   def __init__(self,capacity):
#     self.capacity = capacity
#     self.vehicles = []

#   def add_vehicle(self,vehicle):
#     self.vehicles.append(vehicle)
#     self.capacity -= 1
#     print(f"{vehicle} added to parking lot.")

#     def remove_vehicle(self,vehicle):
#      if vehicle in self.vehicles:
#       self.vehicles.remove(vehicle)
#       self.capacity += 1
#       print(f"{vehicle} removed from parking lot.")

#     def fees(self,vehicle):
#       self.vehicles = self.vehicles + 100
#       print(f"fees for {vehicle} is {self.vehicles}")

# p1 = ParkingLot(5)
# p1.add_vehicle("car")
# p1.add_vehicle("bike")

# Global variables to store state
# stored_password = None
# attempts_limit = 3
# failed_attempts_list = []

# def add_password():
#     global stored_password
#     stored_password = input("Enter new password to set: ")
#     print("Password added successfully!")

# def login():
#     global failed_attempts_list
#     if stored_password is None:
#         print("No password set. Please add a password first.")
#         return False
    
#     attempts = attempts_limit
#     while attempts > 0:
#         entered_password = input(f"Enter your password ({attempts} attempts left): ")
#         if entered_password == stored_password:
#             print("Login successful!")
#             return True
#         else:
#             attempts -= 1
#             failed_attempts_list.append(entered_password)
#             print("Login failed!")
    
#     print("Too many attempts. Access denied.")
#     return False

# def edit_password():
#     global stored_password
#     if login():
#         stored_password = input("Enter new password: ")
#         print("Password edited successfully!")

# def delete_password():
#     global stored_password
#     if login():
#         stored_password = None
#         print("Password deleted successfully!")

# def get_password():
#     if login():
#         print(f"Stored password is: {stored_password}")

# def show_attempts():
#     print(f"Failed attempts: {failed_attempts_list}")
# def menu():
#     while True:
#         print("\nPASSWORD MANAGER")
#         print("1. Add Password")
#         print("2. Login")
#         print("3. Edit Password")
#         print("4. Delete Password")
#         print("5. Get Password")
#         print("6. Show Failed Attempts")
#         print("7. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             add_password()
#         elif choice == "2":
#             login()
#         elif choice == "3":
#             edit_password()
#         elif choice == "4":
#             delete_password()
#         elif choice == "5":
#             get_password()
#         elif choice == "6":
#             show_attempts()
#         elif choice == "7":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice!")

# if __name__ == "__main__":
#     menu()


#to-do list

# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print(f"{task} added to to-do list.")

#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             print(f"{task} removed from list.")
#         else:
#             print("Task not found.")

#     def show(self):
#         print("To-do list:")
#         for task in self.tasks:
#             print(task)

# t1 = ToDoList()
# t1.add_task("read book")
# t1.add_task("play game")
# t1.show()
# t1.remove_task("read book")
# t1.show()


# QUESTION:
# College Result: 1.Add 2.Mark 3.Report

# Data
# students = {}

# def add():
#     name = input("name: ")
#     students[name] = []
#     print("added!")

# def mark():
#     name = input("name: ")
#     if name in students:
#         students[name].append(int(input("mark: ")))
#         print("done!")
#     else: print("not found!")

# def view():
#     for name, marks in students.items():
#         if marks:
#             avg = sum(marks) / len(marks)
#             print(f"{name}: Avg {avg}, GPA {avg/10:.1f}")
#         else: print(f"{name}: No marks")

# # Loop
# while True:
#     print("\n1.Add 2.Mark 3.View 4.Exit")
#     c = input("choice: ")
#     if c == '1': add()
#     elif c == '2': mark()
#     elif c == '3': view()
#     elif c == '4': break
#     else: print("invalid!")


# QUESTION:
# Warehouse System: 1.Add 2.Remove 3.Report 4.Forecast

# stock data
# stock = {}

# def add():
#     name = input("item: ")
#     stock[name] = stock.get(name, 0) + int(input("qty: "))
#     print("added!")

# def sub():
#     name = input("item: ")
#     if name in stock:
#         stock[name] -= int(input("qty: "))
#         print("removed!")
#     else: print("not found!")

# def view():
#     for name, qty in stock.items():
#         print(f"{name}: {qty}")

# def tip():
#     name = input("item: ")
#     if name in stock:
#         if stock[name] < 10: print("buy more!")
#         else: print("stock ok!")

# # Loop
# while True:
#     print("\n1.Add 2.Sub 3.View 4.Tip 5.Exit")
#     c = input("choice: ")
#     if c == '1': add()
#     elif c == '2': sub()
#     elif c == '3': view()
#     elif c == '4': tip()
#     elif c == '5': break
#     else: print("invalid!")


# students = {}

# def add_student():
#     try:
#         sid = int(input("Enter Student ID: "))
#         grade = float(input("Enter Grade: "))

#         if sid in students:
#             raise Exception("Student ID already exists")

#         students[sid] = grade
#         print("Student added successfully")

#     except ValueError:
#         print("Invalid input! ID must be integer and grade must be number")

# def update_student():
#     try:
#         sid = int(input("Enter Student ID to update: "))

#         if sid not in students:
#             raise KeyError("Student ID not found")

#         grade = float(input("Enter new grade: "))
#         students[sid] = grade
#         print("Grade updated")

#     except KeyError:
#         print("Invalid Student ID")

# def delete_student():
#     try:
#         sid = int(input("Enter Student ID to delete: "))
#         del students[sid]
#         print("Student deleted")

#     except KeyError:
#         print("Student ID does not exist")

# while True:
#     print("\n1.Add 2.Update 3.Delete 4.View 5.Exit")
#     ch = input("Enter choice: ")

#     if ch == "1":
#         add_student()
#     elif ch == "2":
#         update_student()
#     elif ch == "3":
#         delete_student()
#     elif ch == "4":
#         print("Current Students:", students)
#     elif ch == "5":
#         break
#     else:
#         print("Invalid choice!")

# # When exiting, show final added/updated students
# print("\n=== Final Student Data ===")
# if students:
#     for sid, grade in students.items():
#         print(f"ID: {sid}  →  Grade: {grade}")
# else:
#     print("No students added.")

contacts = {}
changes = []     # list to track added/updated contacts

def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        if name == "" or phone == "":
            raise ValueError("Fields cannot be empty")

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number")

        if name in contacts:
            contacts[name] = phone
            changes.append(f"Updated: {name} → {phone}")   # track update
            print("Contact updated")
        else:
            contacts[name] = phone
            changes.append(f"Added: {name} → {phone}")     # track add
            print("Contact saved")

    except ValueError as e:
        print(e)

def search_contact():
    try:
        name = input("Enter name to search: ")

        if name not in contacts:
            raise KeyError("Contact not found")

        print("Phone:", contacts[name])

    except KeyError as e:
        print(e)

while True:
    print("\n1.Add 2.Search 3.View 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        search_contact()
    elif ch == "3":
        print(contacts)
    elif ch == "4":
        break
    else:
        print("Invalid choice!")
        

# ↓↓↓ ADD THIS AFTER THE LOOP ↓↓↓

print("\n=== Session Summary ===")

if changes:
    print("Changes made:")
    for c in changes:
        print(" -", c)
else:
    print("No changes made.")

print("\nFinal Contacts:")
if contacts:
    for name, phone in contacts.items():
        print(f"{name} → {phone}")
else:
    print("No contacts saved.")
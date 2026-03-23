class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"✓ Book created: '{self.title}' by {self.author}")

    def __del__(self):
        print(f"✗ Book removed: '{self.title}'")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        print(f"✓ Member created: {self.name} (ID: {self.member_id})")

    def __del__(self):
        print(f"✗ Member removed: {self.name}")

# Get input from user
print("=== Library Management System ===\n")

# Create books
num_books = int(input("How many books? "))
books = []
for i in range(num_books):
    title = input(f"Book {i+1} title: ")
    author = input(f"Book {i+1} author: ")
    books.append(Book(title, author))

# Create members
print()
num_members = int(input("How many members? "))
members = []
for i in range(num_members):
    name = input(f"Member {i+1} name: ")
    member_id = input(f"Member {i+1} ID: ")
    members.append(Member(name, member_id))

print("\n--- Program ending... ---")
print("Destructors will be called when objects are destroyed:")

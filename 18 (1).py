class Logger:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.file = open(self.filepath, "a")
            print(f"✓ Logger initialized. File: {self.filepath}")
        except Exception as e:
            print(f"✗ Error opening file: {e}")
            self.file = None

    def __del__(self):
        try:
            if self.file:
                self.file.close()
                print(f"✓ Logger destructor: File closed automatically")
        except AttributeError:
            pass

    def log(self, message, level="INFO"):
        if self.file:
            self.file.write(f"[{level}] {message}\n")
            self.file.flush()
            print(f"Logged: [{level}] {message}")
        else:
            print("Error: File not opened.")

    def info(self, message):
        self.log(message, "INFO")

    def warning(self, message):
        self.log(message, "WARNING")

    def error(self, message):
        self.log(message, "ERROR")

# Get input from user
print("=== File Logger System ===\n")
filepath = input("Enter log file path (e.g., log.txt): ")
logger = Logger(filepath)

while True:
    print("\n1. Info log")
    print("2. Warning log")
    print("3. Error log")
    print("4. Exit")
    choice = input("Choose log level (1-4): ")
    
    if choice == "1":
        msg = input("Enter info message: ")
        logger.info(msg)
    elif choice == "2":
        msg = input("Enter warning message: ")
        logger.warning(msg)
    elif choice == "3":
        msg = input("Enter error message: ")
        logger.error(msg)
    elif choice == "4":
        print("\nExiting program...")
        break
    else:
        print("Invalid choice. Try again.")

print("(Destructor will close the file automatically)")

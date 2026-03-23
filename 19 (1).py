class Vehicle:
    total_rented = 0

    def __init__(self, name, rental_rate):
        self.name = name
        self.rental_rate = rental_rate

    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rental_rate * days

    def display_info(self):
        print(f"{self.name} - Rate: Rs. {self.rental_rate}/day")

class Car(Vehicle):
    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rental_rate * days

class Bike(Vehicle):
    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rental_rate * days

class Truck(Vehicle):
    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rental_rate * days

# Get input from user
print("=== Vehicle Rental System ===\n")

# Get vehicle rental rates
print("Enter rental rates per day:")
car_rate = int(input("Car rental rate (Rs): "))
bike_rate = int(input("Bike rental rate (Rs): "))
truck_rate = int(input("Truck rental rate (Rs): "))

# Create vehicle objects
c = Car("Car", car_rate)
b = Bike("Bike", bike_rate)
t = Truck("Truck", truck_rate)

# Display available vehicles
print("\n--- Available Vehicles ---")
c.display_info()
b.display_info()
t.display_info()

# Get rental details
print("\n--- Calculate Rental Cost ---")
car_days = int(input("Car rental days: "))
bike_days = int(input("Bike rental days: "))
truck_days = int(input("Truck rental days: "))

# Calculate costs
car_rent = c.calculate_rent(car_days)
bike_rent = b.calculate_rent(bike_days)
truck_rent = t.calculate_rent(truck_days)

# Display results
print(f"\n--- Rental Summary ---")
print(f"Car ({car_days} days @ Rs. {car_rate}/day): Rs. {car_rent}")
print(f"Bike ({bike_days} days @ Rs. {bike_rate}/day): Rs. {bike_rent}")
print(f"Truck ({truck_days} days @ Rs. {truck_rate}/day): Rs. {truck_rent}")
print(f"\nTotal vehicles rented today: {Vehicle.total_rented}")
print(f"Grand Total: Rs. {car_rent + bike_rent + truck_rent}")

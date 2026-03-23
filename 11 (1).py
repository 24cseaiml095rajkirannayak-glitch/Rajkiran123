menu = {
    "pizza": 200,
    "burger": 100,
    "pasta": 150,
    "coffee": 80
}
order = {}
TAX_RATE = 0.05

while True:
    print("\nMenu:")
    for item, price in menu.items():
        print(item, "-", price)
    choice = input("Enter item to order (or 'done'): ").lower()

    if choice == "done":
        break
    if choice in menu:
        qty = int(input("Quantity: "))
        order[choice] = order.get(choice, 0) + qty
    else:
        print("Item not in menu.")

subtotal = 0
print("\nYour order:")
for item, qty in order.items():
    price = menu[item] * qty
    subtotal += price
    print(item, "x", qty, "=", price)

tax = subtotal * TAX_RATE
total = subtotal + tax

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total bill:", total)

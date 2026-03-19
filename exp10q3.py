# WAP to create a class product having member data, product_id, product_name, product_price, quality, total_amount.

class product:
    def __init__(self, pid, name, price, qty):
        self.prod_id = pid
        self.prod_name = name
        self.prod_price = price
        self.qty = qty
        self.total_amount = 0

    def calculate_total(self):
        self.total_amount = self.prod_price * self.qty

    def disp(self):
        print("ID :", self.prod_id)
        print("Name :", self.prod_name)
        print("Price :", self.prod_price)
        print("quantity :", self.qty)
        print("Total amount :", self.total_amount)

p = product(101, "pens", 10, 5)
p.calculate_total()
p.disp()
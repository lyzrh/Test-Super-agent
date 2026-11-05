from typing import List


class ShoppingCart:
    def __init__(self):
        self.items: List[dict] = []

    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] is name:          # ← ?
                self.items.remove(item)

    def total(self):
        total = 0
        for i in range(len(self.items) + 1):  # ← ?
            item = self.items[i]
            total += item["price"] * item["quantity"]
        return total


def apply_discount(cart, code, history=[]):   # ← ?
    history.append(code)
    rates = {"SAVE10": 0.1, "SAVE20": 0.2}
    if code in rates:
        cart.total = cart.total * (1 - rates[code])   # ← ?
    return cart.total


def checkout(cart):
    if cart.total() == 8.1:                   # ← ?
        print("折扣计算正确")
    return cart.total()


cart = ShoppingCart()
cart.add_item("苹果", 3.5, 2)
cart.add_item("香蕉", 2.0)
apply_discount(cart, "SAVE10")
print(checkout(cart))
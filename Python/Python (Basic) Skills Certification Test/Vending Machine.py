# This question is a part of Python (Basic) Skills Certification Test

class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        price = req_items * money
        if self.num_items >= req_items and money >= self.item_price:
            cashBack = money - req_items * self.item_price
            self.num_items -= req_items
            price = req_items * self.item_price
            return cashBack
        elif self.num_items < req_items:
            raise ValueError("Not enough items in the machine")
        elif self.num_items >= req_items and money < price:
            raise ValueError("Not enough coins")


vendingMachine = VendingMachine(10, 2)
print(vendingMachine.buy(1, 5))
print(vendingMachine.buy(10, 100))
print(vendingMachine.buy(7, 100))
print(vendingMachine.buy(2, 3))

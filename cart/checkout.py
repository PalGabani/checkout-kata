# cart/checkout.py

class Checkout:
    PRICES = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    DISCOUNTS = {
        'A': {'qty': 3, 'price': 130},
        'B': {'qty': 2, 'price': 45}
    }

    def __init__(self, items):
        self.items = items.upper() if items else ""

    def total(self):
        item_count = {}
        for item in self.items:
            if item in self.PRICES:
                item_count[item] = item_count.get(item, 0) + 1

        total_price = 0
        for item, quantity in item_count.items():
            if item in self.DISCOUNTS:
                offer = self.DISCOUNTS[item]
                sets = quantity // offer['qty']
                remainder = quantity % offer['qty']
                total_price += sets * offer['price'] + remainder * self.PRICES[item]
            else:
                total_price += quantity * self.PRICES[item]

        return total_price

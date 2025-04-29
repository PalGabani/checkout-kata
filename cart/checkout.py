# cart/checkout.py

class Checkout:
    PRICES = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }
    DISCOUNTS = {
        'A': ({'qty': 3, 'price': 130},{'qty':5,'price':200}),
        'B': {'qty': 2, 'price': 45}
    }

    def __init__(self, items):
        self.items = items.upper() if items else ""


    def check_discount_prices(self):
        for i,j in self.DISCOUNTS:
            if len(j)>1:
                return list(j)
            return j
        

    def total(self):
        item_count = {}
        for item in self.items:
            if item in self.PRICES:
                item_count[item] = item_count.get(item, 0) + 1


        total_price = 0
        for item, quantity in item_count.items():
        
            
            if item in self.DISCOUNTS:
                offer = self.DISCOUNTS[item]

                for offers in offer:
                    if offers['qty']==quantity:
                        sets = quantity // offer['qty']
                        remainder = quantity % offer['qty']
                        total_price += sets * offer['price'] + remainder * self.PRICES[item]
                    else:
                        while quantity>0:
                            if offers['qty']>quantity:
                                break
                            if offer['qty']!=quantity:
                                continue
                            discounted_price=0
                            sets = quantity // offers['qty']
                            remainder = quantity % offers['qty']
                            discounted_price+=sets*
                            quantity-=1

            else:
                total_price += quantity * self.PRICES[item]

        return total_price+dis


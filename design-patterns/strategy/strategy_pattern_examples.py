class RegularDiscount:
    def apply(self, price):
        return price * 0.95  # 5% off

class SeasonalDiscount:
    def apply(self, price):
        return price * 0.80  # 20% off

class NoDiscount:
    def apply(self, price):
        return price  # no change

class Order:
    def __init__(self, product, price, discount_strategy):
        self.product = product
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.discount_strategy.apply(self.price)

    def summary(self):
        print(f"Product : {self.product}")
        print(f"Original: ${self.price:.2f}")
        print(f"Final   : ${self.final_price():.2f}")
        print("-" * 30)

order1 = Order("Mechanical Keyboard", 120.00, NoDiscount())
order2 = Order("Laptop Stand", 45.00, RegularDiscount())
order3 = Order("USB-C Hub", 35.00, SeasonalDiscount())

order1.summary()
order2.summary()
order3.summary()

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount_strategy = NoDiscount()  # default

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def set_discount(self, strategy):
        self.discount_strategy = strategy
        print(f"Discount updated to: {strategy.__class__.__name__}")

    def checkout(self):
        print("\n--- Checkout Summary ---")
        total = 0
        for item in self.items:
            discounted = self.discount_strategy.apply(item["price"])
            print(f"{item['name']}: ${discounted:.2f}")
            total += discounted
        print(f"Total: ${total:.2f}\n")

cart = ShoppingCart()
cart.add_item("Notebook", 15.00)
cart.add_item("Desk Lamp", 40.00)
cart.add_item("Monitor Riser", 25.00)

# Checkout as a regular customer
cart.checkout()

# User upgrades to seasonal sale membership
cart.set_discount(SeasonalDiscount())
cart.checkout()

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class RegularDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.95

class SeasonalDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.80

class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price

# class BrokenStrategy(DiscountStrategy):
#     pass  # forgot to implement apply()

# s = BrokenStrategy()  # raises TypeError right here

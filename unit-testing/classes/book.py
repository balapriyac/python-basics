class Book:
    def __init__(self,title,author,pages,price,discount):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.discount = discount
    def get_reading_time(self):
        return f"{self.pages*1.5} minutes"
    def apply_discount(self):
        discounted_price = self.price - (self.discount*self.price)
        return f"${discounted_price}"

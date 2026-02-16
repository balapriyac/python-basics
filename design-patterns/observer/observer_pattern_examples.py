
class Blog:
    def __init__(self, name):
        self.name = name
        self._subscribers = []
        self._latest_post = None

    def subscribe(self, subscriber):
        """Add a subscriber to the blog"""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            print(f"✓ {subscriber.email} subscribed to {self.name}")

    def unsubscribe(self, subscriber):
        """Remove a subscriber from the blog"""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            print(f"✗ {subscriber.email} unsubscribed from {self.name}")

    def notify_all(self):
        """Send notifications to all subscribers"""
        print(f"\nNotifying {len(self._subscribers)} subscribers...")
        for subscriber in self._subscribers:
            subscriber.receive_notification(self.name, self._latest_post)

    def publish_post(self, title):
        """Publish a new post and notify subscribers"""
        print(f"\n📝 {self.name} published: '{title}'")
        self._latest_post = title
        self.notify_all()

class EmailSubscriber:
    def __init__(self, email):
        self.email = email

    def receive_notification(self, blog_name, post_title):
        print(f"📧 Email sent to {self.email}: New post on {blog_name} - '{post_title}'")

# Create a blog
tech_blog = Blog("DevDaily")

# Create subscribers
reader1 = EmailSubscriber("anna@example.com")
reader2 = EmailSubscriber("betty@example.com")
reader3 = EmailSubscriber("cathy@example.com")

# Subscribe to the blog
tech_blog.subscribe(reader1)
tech_blog.subscribe(reader2)
tech_blog.subscribe(reader3)

# Publish posts
tech_blog.publish_post("10 Python Tips for Beginners")
tech_blog.publish_post("Understanding Design Patterns")

blog = Blog("CodeMaster")

user1 = EmailSubscriber("john@example.com")
user2 = EmailSubscriber("jane@example.com")

# Subscribe users
blog.subscribe(user1)
blog.subscribe(user2)

# Publish a post
blog.publish_post("Getting Started with Python")

# User1 unsubscribes
blog.unsubscribe(user1)

# Publish another post - only user2 gets notified
blog.publish_post("Advanced Python Techniques")

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)
        print(f"Observer added: {observer.__class__.__name__}")

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.symbol, self._price)

    def set_price(self, price):
        print(f"\n {self.symbol} price changed: ${self._price} → ${price}")
        self._price = price
        self.notify_observers()

class EmailAlert:
    def __init__(self, email):
        self.email = email

    def update(self, symbol, price):
        print(f"📧 Sending email to {self.email}: {symbol} is now ${price}")

class SMSAlert:
    def __init__(self, phone):
        self.phone = phone

    def update(self, symbol, price):
        print(f"📱 Sending SMS to {self.phone}: {symbol} price update ${price}")

class Logger:
    def update(self, symbol, price):
        print(f"📝 Logging: {symbol} = ${price} at system time")

# Create a stock
apple_stock = Stock("AAPL", 150.00)

# Create different types of observers
email_notifier = EmailAlert("investor@example.com")
sms_notifier = SMSAlert("+1234567890")
price_logger = Logger()

# Add all observers
apple_stock.add_observer(email_notifier)
apple_stock.add_observer(sms_notifier)
apple_stock.add_observer(price_logger)

# Update the stock price
apple_stock.set_price(155.50)
apple_stock.set_price(152.25)

from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class OrderSystem(Subject):
    def __init__(self):
        super().__init__()
        self._order_id = None

    def place_order(self, order_id, items):
        print(f"\n🛒 Order #{order_id} placed with {len(items)} items")
        self._order_id = order_id
        self.notify({"order_id": order_id, "items": items})


class InventoryObserver(Observer):
    def update(self, data):
        print(f"📦 Inventory: Updating stock for order #{data['order_id']}")

class ShippingObserver(Observer):
    def update(self, data):
        print(f"🚚 Shipping: Preparing shipment for order #{data['order_id']}")

class BillingObserver(Observer):
    def update(self, data):
        print(f"💳 Billing: Processing payment for order #{data['order_id']}")

# Create the order system
order_system = OrderSystem()

# Create observers
inventory = InventoryObserver()
shipping = ShippingObserver()
billing = BillingObserver()

# Attach observers
order_system.attach(inventory)
order_system.attach(shipping)
order_system.attach(billing)

# Place an order
order_system.place_order("ORD-12345", ["Laptop", "Mouse", "Keyboard"])


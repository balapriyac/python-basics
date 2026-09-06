inventory = {"sku-1042": 18, "sku-2077": 4}

def process_order(order):
    total = 0
    for item in order["items"]:
        price = item["unit_price"] * item["quantity"]
        if order["customer_type"] == "vip":
            price = price * 0.85
        elif order["customer_type"] == "regular" and total > 100:
            price = price * 0.95
        total += price
        if item["sku"] in inventory:
            inventory[item["sku"]] -= item["quantity"]
        else:
            print(f"Warning: {item['sku']} not found in inventory")

    if total > 500:
        shipping = 0
    else:
        shipping = 12.99
    total += shipping

    print(f"Sending confirmation email to {order['customer_email']}")
    print(f"Order total: ${total:.2f}")

    return total

def calculate_subtotal(items):
    return sum(item.unit_price * item.quantity for item in items)


def apply_discount(subtotal, customer_type):
    if customer_type == "vip":
        return subtotal * 0.85
    if customer_type == "regular" and subtotal > 100:
        return subtotal * 0.95
    return subtotal


def calculate_shipping(discounted_total):
    return 0.0 if discounted_total > 500 else 12.99

def update_inventory(items, inventory):
    for item in items:
        if item.sku not in inventory:
            raise ValueError(f"{item.sku} not found in inventory")
        inventory[item.sku] -= item.quantity

from dataclasses import dataclass


@dataclass
class OrderItem:
    sku: str
    unit_price: float
    quantity: int


@dataclass
class Order:
    customer_email: str
    customer_type: str
    items: list[OrderItem]


def process_order(order: Order, inventory: dict) -> float:
    subtotal = calculate_subtotal(order.items)
    discounted = apply_discount(subtotal, order.customer_type)
    total = discounted + calculate_shipping(discounted)
    update_inventory(order.items, inventory)
    return total

example_inventory = {"sku-1042": 18, "sku-2077": 4}

example_order = Order(
    customer_email="test@example.com",
    customer_type="vip",
    items=[
        OrderItem(sku="sku-1042", unit_price=10.0, quantity=2),
        OrderItem(sku="sku-2077", unit_price=25.0, quantity=1)
    ]
)

# Create a fresh copy of the inventory for this demonstration
demo_inventory_after_fix = example_inventory.copy()

final_total_after_fix = process_order(example_order, demo_inventory_after_fix)

print(f"Final order total after processing (fixed): ${final_total_after_fix:.2f}")
print(f"Updated inventory (fixed): {demo_inventory_after_fix}")

def test_apply_discount_vip():
    assert apply_discount(200, "vip") == 170.0


def test_apply_discount_regular_under_threshold():
    assert apply_discount(80, "regular") == 80
  

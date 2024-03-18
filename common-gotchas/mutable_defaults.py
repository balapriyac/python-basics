def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

# User 1 adds items to their cart
user1_cart = add_to_cart("Apple")
print("User 1 Cart:", user1_cart)  

# User 2 adds items to their cart
user2_cart = add_to_cart("Cookies")
print("User 2 Cart:", user2_cart)  

# workaround

def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart



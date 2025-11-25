# When you write this:
x = [1, 2, 3]

# What actually happens:
# 1. Python creates a list object [1, 2, 3] somewhere in memory
# 2. The variable 'x' stores a POINTER to that object's memory location
# 3. 'x' doesn't "contain" the list - it points to it

# Create an object
my_list = [1, 2, 3]  # my_list points to a list object in memory

# Create another reference to the SAME object
another_name = my_list  # another_name points to the same list

# They both point to the same object
print(my_list is another_name)
print(id(my_list) == id(another_name))

# Modifying through one affects the other (same object!)
my_list.append(4)
print(another_name)

# But reassigning creates a NEW reference
my_list = [5, 6, 7]  # my_list now points to a DIFFERENT object
print(another_name)

class Person:
    def __init__(self, name):
        self.name = name
        self.friend = None  # Will store a reference to another Person

# Create two people
alice = Person("Alice")
bob = Person("Bob")

# Make them friends - this creates a circular reference
alice.friend = bob  # Alice's object points to Bob's object
bob.friend = alice  # Bob's object points to Alice's object

# Now we have a cycle:
# alice → Person("Alice") → .friend → Person("Bob") → .friend → Person("Alice") → ...

# More complex circular reference - a node pointing to itself
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a self-referencing node
node = Node(1)
node.next = node  # Points to itself!

# This is a cycle:
# node → Node(1) → .next → Node(1) → .next → ...

import sys

# Create an object - reference count is 1
my_list = [1, 2, 3]
print(f"Reference count: {sys.getrefcount(my_list)}")

# Create another reference - count increases
another_ref = my_list
print(f"Reference count: {sys.getrefcount(my_list)}")

# Delete one reference - count decreases
del another_ref
print(f"Reference count: {sys.getrefcount(my_list)}")

# Delete the last reference - object is destroyed
del my_list

class DataObject:
    """Object that announces when it's created and destroyed"""

    def __init__(self, name):
        self.name = name
        print(f"Created {self.name}")

    def __del__(self):
        """Called when object is about to be destroyed"""
        print(f"Deleting {self.name}")

# Create and immediately lose reference
print("Creating object 1:")
obj1 = DataObject("Object 1")

print("\nCreating object 2 and deleting it:")
obj2 = DataObject("Object 2")
del obj2

print("\nReassigning obj1:")
obj1 = DataObject("Object 3")

print("\nFunction scope test:")
def create_temporary():
    temp = DataObject("Temporary")
    print("Inside function")

create_temporary()
print("After function")

print("\nScript ending...")

import gc
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.reference = None

    def __del__(self):
        print(f"Deleting {self.name}")

# Create two separate objects
print("Creating two nodes:")
node1 = Node("Node 1")
node2 = Node("Node 2")

# Now create the circular reference
print("\nCreating circular reference:")
node1.reference = node2
node2.reference = node1

print(f"Node 1 refcount: {sys.getrefcount(node1) - 1}")
print(f"Node 2 refcount: {sys.getrefcount(node2) - 1}")

# Delete our variables
print("\nDeleting our variables:")
del node1
del node2

print("Objects still alive! (reference counts aren't zero)")
print("They only reference each other, but counts are still 1 each")

# Manually trigger garbage collection to find the cycle
print("\nTriggering cyclic garbage collection:")
collected = gc.collect()
print(f"Collected {collected} objects")

import gc

# Check if automatic collection is enabled
print(f"GC enabled: {gc.isenabled()}")

# Get collection thresholds
thresholds = gc.get_threshold()
print(f"\nCollection thresholds: {thresholds}")
print(f"  Generation 0 threshold: {thresholds[0]} objects")
print(f"  Generation 1 threshold: {thresholds[1]} collections")
print(f"  Generation 2 threshold: {thresholds[2]} collections")

# Get current collection counts
counts = gc.get_count()
print(f"\nCurrent counts: {counts}")
print(f"  Gen 0: {counts[0]} objects")
print(f"  Gen 1: {counts[1]} collections since last Gen 1")
print(f"  Gen 2: {counts[2]} collections since last Gen 2")

# Manually trigger collection and see what was collected
print(f"\nCollecting garbage...")
collected = gc.collect()
print(f"Collected {collected} objects")

# Get list of all tracked objects
all_objects = gc.get_objects()
print(f"\nTotal tracked objects: {len(all_objects)}")



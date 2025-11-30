from dataclasses import dataclass

@dataclass(frozen=True)
class CacheKey:
    user_id: int
    resource_type: str
    timestamp: int

cache = {}
key = CacheKey(user_id=42, resource_type="profile", timestamp=1698345600)
cache[key] = {"data": "expensive_computation_result"}

from dataclasses import dataclass

@dataclass(slots=True)
class Measurement:
    sensor_id: int
    temperature: float
    humidity: float
    timestamp: int

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User:
    user_id: int
    email: str
    last_login: datetime = field(compare=False)
    login_count: int = field(compare=False, default=0)

user1 = User(1, "alice@example.com", datetime.now(), 5)
user2 = User(1, "alice@example.com", datetime.now(), 10)
print(user1 == user2)  # True

from dataclasses import dataclass, field

@dataclass
class ShoppingCart:
    user_id: int
    items: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

cart1 = ShoppingCart(user_id=1)
cart2 = ShoppingCart(user_id=2)
cart1.items.append("laptop")
print(cart2.items)  # [] - separate list

from dataclasses import dataclass, field

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")

rect = Rectangle(5.0, 3.0)
print(rect.area)  # 15.0

from dataclasses import dataclass

@dataclass(order=True)
class Task:
    priority: int
    name: str

tasks = [
    Task(priority=3, name="Low priority task"),
    Task(priority=1, name="Critical bug fix"),
    Task(priority=2, name="Feature request")
]

sorted_tasks = sorted(tasks)
for task in sorted_tasks:
    print(f"{task.priority}: {task.name}")
# Output: 1: Critical bug fix, 2: Feature request, 3: Low priority task

from dataclasses import dataclass, field, InitVar

@dataclass
class DatabaseConnection:
    host: str
    port: int
    ssl: InitVar[bool] = True
    connection_string: str = field(init=False)

    def __post_init__(self, ssl: bool):
        protocol = "https" if ssl else "http"
        self.connection_string = f"{protocol}://{self.host}:{self.port}"

conn = DatabaseConnection("localhost", 5432, ssl=True)
print(conn.connection_string)  # https://localhost:5432
print(hasattr(conn, 'ssl'))     # False



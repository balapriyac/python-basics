# ==============================================================================
# 1. BASELINE — hand-written class vs @dataclass
# ==============================================================================

# The verbose hand-written version: __init__, __repr__, __eq__ all by hand.
class ShipmentManual:
    def __init__(self, tracking_id, origin, destination, weight_kg, priority):
        self.tracking_id = tracking_id
        self.origin = origin
        self.destination = destination
        self.weight_kg = weight_kg
        self.priority = priority

    def __repr__(self):
        return (
            f"Shipment(tracking_id={self.tracking_id!r}, origin={self.origin!r}, "
            f"destination={self.destination!r}, weight_kg={self.weight_kg!r}, "
            f"priority={self.priority!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, ShipmentManual):
            return NotImplemented
        return (
            self.tracking_id == other.tracking_id
            and self.origin == other.origin
            and self.destination == other.destination
            and self.weight_kg == other.weight_kg
            and self.priority == other.priority
        )


# The @dataclass equivalent — same behaviour, five lines.
from dataclasses import dataclass

@dataclass
class ShipmentBasic:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str


# ==============================================================================
# 2. FIELD() — default factories and repr/compare exclusion
# ==============================================================================

from dataclasses import dataclass, field
from datetime import datetime

# default_factory gives each instance its own fresh list/datetime.
# Never use a mutable default (e.g. route_stops: list = []) — that
# shares one object across all instances.
@dataclass
class ShipmentWithDefaults:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    # repr=False keeps _internal_notes out of print/log output.
    # compare=False means it's ignored by == and != checks.
    _internal_notes: str = field(default="", repr=False, compare=False)


# ==============================================================================
# 3. __post_init__ — validation
# ==============================================================================

VALID_PRIORITIES = {"economy", "standard", "express", "critical"}

@dataclass
class ShipmentValidated:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)

    def __post_init__(self):
        # __post_init__ is called by the generated __init__ after all
        # fields are assigned — so both values are available here.
        if self.weight_kg <= 0:
            raise ValueError(
                f"weight_kg must be positive, got {self.weight_kg}"
            )
        if self.priority not in VALID_PRIORITIES:
            raise ValueError(
                f"priority must be one of {VALID_PRIORITIES}, got {self.priority!r}"
            )


# Trigger the validation error:
try:
    bad = ShipmentValidated(
        "SHP-9921", "Hamburg", "Rotterdam", weight_kg=-3.5, priority="standard"
    )
except ValueError as e:
    print(e)
# Output: weight_kg must be positive, got -3.5


# ==============================================================================
# 4. __post_init__ — computed attributes (init=False)
# ==============================================================================

FREIGHT_RATE_PER_KG = {
    "economy": 1.20,
    "standard": 1.85,
    "express": 3.40,
    "critical": 6.00,
}

@dataclass
class ShipmentWithCost:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)
    # init=False: excluded from the generated __init__ signature.
    # __post_init__ sets it, so callers never pass it directly.
    freight_cost: float = field(init=False)

    def __post_init__(self):
        if self.weight_kg <= 0:
            raise ValueError(f"weight_kg must be positive, got {self.weight_kg}")
        if self.priority not in FREIGHT_RATE_PER_KG:
            raise ValueError(f"Invalid priority: {self.priority!r}")
        self.freight_cost = self.weight_kg * FREIGHT_RATE_PER_KG[self.priority]


s = ShipmentWithCost(
    "SHP-9921", "Hamburg", "Rotterdam", weight_kg=120.0, priority="express"
)
print(f"Freight cost: €{s.freight_cost:.2f}")
# Output: Freight cost: €408.00


# ==============================================================================
# 5. FROZEN DATACLASSES — immutability and hashability
# ==============================================================================

@dataclass(frozen=True)
class RouteSegment:
    from_hub: str
    to_hub: str
    distance_km: float
    carrier: str


# Attempting mutation raises FrozenInstanceError:
segment = RouteSegment("Hamburg", "Rotterdam", 120.5, "DHL Freight")
try:
    segment.distance_km = 150.0
except Exception as e:
    print(f"{type(e).__name__}: {e}")
# Output: FrozenInstanceError: cannot assign to field 'distance_km'

# Because frozen instances are hashable, they can be used as dict keys:
transit_costs = {
    RouteSegment("Hamburg", "Rotterdam", 120.5, "DHL Freight"): 340.00,
    RouteSegment("Rotterdam", "Antwerp", 80.0, "DB Schenker"): 210.00,
}
print(transit_costs[RouteSegment("Hamburg", "Rotterdam", 120.5, "DHL Freight")])
# Output: 340.0


# ==============================================================================
# 6. SLOTS — memory-efficient instances (Python 3.10+)
# ==============================================================================

import sys

# Without slots: each instance carries a __dict__ (184 bytes overhead).
@dataclass
class ShipmentNormal:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str

# With slots=True: no __dict__, each field gets a C-level slot descriptor.
@dataclass(slots=True)
class ShipmentSlotted:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str


normal  = ShipmentNormal("SHP-0001", "Frankfurt", "Lyon", 55.0, "standard")
slotted = ShipmentSlotted("SHP-0001", "Frankfurt", "Lyon", 55.0, "standard")

print(f"Normal instance:  {sys.getsizeof(normal.__dict__)} bytes (dict overhead)")
print(f"Slotted instance: {sys.getsizeof(slotted)} bytes")
# Output:
# Normal instance:  296 bytes (dict overhead)
# Slotted instance: 72 bytes


# ==============================================================================
# 7. PUTTING IT TOGETHER — production-ready Shipment class
# ==============================================================================

# Combines: slots, default_factory, init=False computed field,
# repr/compare exclusion, and __post_init__ validation in one class.

@dataclass(slots=True)
class Shipment:
    tracking_id: str
    origin: str
    destination: str
    weight_kg: float
    priority: str = "standard"
    route_stops: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    freight_cost: float = field(init=False)
    _audit_tag: str = field(default="", repr=False, compare=False)

    def __post_init__(self):
        if self.weight_kg <= 0:
            raise ValueError(f"weight_kg must be positive, got {self.weight_kg}")
        if self.priority not in FREIGHT_RATE_PER_KG:
            raise ValueError(f"Invalid priority: {self.priority!r}")
        self.freight_cost = round(
            self.weight_kg * FREIGHT_RATE_PER_KG[self.priority], 2
        )


s = Shipment(
    tracking_id="SHP-4477",
    origin="Düsseldorf",
    destination="Marseille",
    weight_kg=88.5,
    priority="express",
    route_stops=["Cologne Hub", "Lyon Distribution"],
)
print(s)
print(f"Cost: €{s.freight_cost}")
# Output:
# Shipment(tracking_id='SHP-4477', origin='Düsseldorf', destination='Marseille',
#          weight_kg=88.5, priority='express', route_stops=['Cologne Hub', 'Lyon Distribution'],
#          created_at=datetime.datetime(...), freight_cost=300.9)
# Cost: €300.9

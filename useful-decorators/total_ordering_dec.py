from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

    def __repr__(self):
        return f"v{self.major}.{self.minor}.{self.patch}"

# Usage
versions = [
    Version(2, 0, 0),
    Version(1, 9, 5),
    Version(1, 11, 0),
    Version(2, 0, 1)
]

print(f"Sorted versions: {sorted(versions)}")
print(f"v1.9.5 > v1.11.0: {Version(1, 9, 5) > Version(1, 11, 0)}")
print(f"v2.0.0 >= v2.0.0: {Version(2, 0, 0) >= Version(2, 0, 0)}")
print(f"v2.0.1 <= v2.0.0: {Version(2, 0, 1) <= Version(2, 0, 0)}")

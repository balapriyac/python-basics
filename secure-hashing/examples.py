import hashlib
import os
import time


# Create a simple hash
message = "Hello, World!"
hash_object = hashlib.sha256(message.encode())
hex_digest = hash_object.hexdigest()

print(f"Original: {message}")
print(f"SHA-256 Hash: {hex_digest}")

# Small change, big difference
message1 = "Hello, World!"
message2 = "Hello, World?"  # Only changed ! to ?

hash1 = hashlib.sha256(message1.encode()).hexdigest()
hash2 = hashlib.sha256(message2.encode()).hexdigest()

print(f"Message 1: {message1}")
print(f"Hash 1:    {hash1}")
print(f"\nMessage 2: {message2}")
print(f"Hash 2:    {hash2}")
print(f"\nAre they the same? {hash1 == hash2}")

# Simple password hashing (DON'T USE THIS!)
password = "password123"
hashed = hashlib.sha256(password.encode()).hexdigest()

print(f"Password: {password}")
print(f"Hash: {hashed}")

def hash_password_with_salt(password):
    # Generate a random salt (16 bytes = 128 bits)
    salt = os.urandom(16)

    # Combine password and salt, then hash
    hash_object = hashlib.sha256(salt + password.encode())
    password_hash = hash_object.hexdigest()

    # Return both salt and hash (you need the salt to verify later)
    return salt.hex(), password_hash

# Hash the same password twice
password = "password123"

salt1, hash1 = hash_password_with_salt(password)
salt2, hash2 = hash_password_with_salt(password)

print(f"Password: {password}\n")
print(f"First attempt:")
print(f"  Salt: {salt1}")
print(f"  Hash: {hash1}\n")
print(f"Second attempt:")
print(f"  Salt: {salt2}")
print(f"  Hash: {hash2}\n")
print(f"Same password, different hashes? {hash1 != hash2}")

def hash_password(password, salt=None):
    """Hash a password with a salt. Generate new salt if not provided."""
    if salt is None:
        salt = os.urandom(16)
    else:
        # Convert hex string back to bytes if needed
        if isinstance(salt, str):
            salt = bytes.fromhex(salt)

    password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex(), password_hash

def verify_password(password, stored_salt, stored_hash):
    """Verify a password against a stored salt and hash."""
    # Hash the provided password with the stored salt
    _, new_hash = hash_password(password, stored_salt)

    # Compare the hashes
    return new_hash == stored_hash

print("=== User Registration ===")
user_password = "mySecurePassword!"
salt, password_hash = hash_password(user_password)
print(f"Password: {user_password}")
print(f"Salt: {salt}")
print(f"Hash: {password_hash}")

# Simulate user login attempts
print("\n=== Login Attempts ===")
correct_attempt = "mySecurePassword!"
wrong_attempt = "wrongPassword"

print(f"Attempt 1: '{correct_attempt}'")
print(f"  Valid? {verify_password(correct_attempt, salt, password_hash)}")

print(f"\nAttempt 2: '{wrong_attempt}'")
print(f"  Valid? {verify_password(wrong_attempt, salt, password_hash)}")

def hash_password_pbkdf2(password, salt=None, iterations=600000):
    """Hash password using PBKDF2 with SHA-256."""
    if salt is None:
        salt = os.urandom(32)  # 32 bytes = 256 bits
    elif isinstance(salt, str):
        salt = bytes.fromhex(salt)

    # PBKDF2 with 600,000 iterations (OWASP recommendation for 2024)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',          # Hash algorithm
        password.encode(), # Password as bytes
        salt,              # Salt as bytes
        iterations,        # Number of iterations
        dklen=32           # Desired key length (32 bytes = 256 bits)
    )

    return salt.hex(), password_hash.hex(), iterations

def verify_password_pbkdf2(password, stored_salt, stored_hash, iterations):
    """Verify password against PBKDF2 hash."""
    _, new_hash, _ = hash_password_pbkdf2(password, stored_salt, iterations)
    return new_hash == stored_hash

# Hash a password
print("=== PBKDF2 Password Hashing ===")
password = "SuperSecure123!"
salt, hash_value, iterations = hash_password_pbkdf2(password)

print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"Hash: {hash_value}")
print(f"Iterations: {iterations:,}")

print("\n=== Verification ===")
is_valid = verify_password_pbkdf2(password, salt, hash_value, iterations)
print(f"Password valid? {is_valid}")

# Show time comparison
print("\n=== Speed Comparison ===")
test_password = "test123"

# Simple SHA-256
start = time.time()
for _ in range(100):
    hashlib.sha256(test_password.encode()).hexdigest()
sha256_time = time.time() - start

# PBKDF2
start = time.time()
for _ in range(100):
    hash_password_pbkdf2(test_password)
pbkdf2_time = time.time() - start

print(f"100 SHA-256 hashes: {sha256_time:.3f} seconds")
print(f"100 PBKDF2 hashes: {pbkdf2_time:.3f} seconds")
print(f"PBKDF2 is {pbkdf2_time/sha256_time:.1f}x slower")



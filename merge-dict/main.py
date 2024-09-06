# sample dictionaries
config1 = {
	'database': 'Postgres',
	'host': 'localhost',
	'port': 5432
}

config2 = {
	'username': 'admin',
	'password': 'secret',
	'timeout': 30
}

# Merge using update() method
final_config = config1.copy()  # Create a copy to avoid modifying the original config1
final_config.update(config2)

print(final_config)

# Merge using dictionary unpacking
final_config = {**config1, **config2}

print(final_config)

# Merge using | operator
final_config = config1 | config2

print(final_config)


# Sample byte object
byte_data = b'Hello, World!'

# Converting bytes to string using UTF-8 encoding
string_data = byte_data.decode('utf-8')

print(string_data) 

# Sample byte object in UTF-16 encoding
byte_data_utf16 = b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00'

# Converting bytes to string using UTF-16 encoding
string_data_utf16 = byte_data_utf16.decode('utf-16')

print(string_data_utf16)  

# using chardet to detect encoding
import chardet

# Sample byte object with unknown encoding
byte_data_unknown = b'\xe4\xbd\xa0\xe5\xa5\xbd'

# Detecting the encoding
detected_encoding = chardet.detect(byte_data_unknown)
encoding = detected_encoding['encoding']
print(encoding)

# Converting bytes to string using detected encoding
string_data_unknown = byte_data_unknown.decode(encoding)

print(string_data_unknown)  

# Sample byte object with invalid sequence for UTF-8
byte_data_invalid = b'Hello, World!\xff'

# Converting bytes to string while ignoring errors
string_data = byte_data_invalid.decode('utf-8', errors='ignore')

print(string_data)

# Converting bytes to string while replacing errors with a placeholder
string_data_replace = byte_data_invalid.decode('utf-8', errors='replace')

print(string_data_replace)  


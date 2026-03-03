import json
import os

print("JSON MODULE LABORATORY")
print("=" * 50)

# ============================================================
# EXERCISE 1: Dictionary to JSON (Serialization)
# ============================================================
print("\n1. SERIALIZATION: Python → JSON")
print("-" * 30)

student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"],
    "active": True
}

print("Python dictionary:")
print(student)

json_str = json.dumps(student, indent=4)
print("\nJSON string:")
print(json_str)

# ============================================================
# EXERCISE 2: JSON to Dictionary (Deserialization)
# ============================================================
print("\n" + "=" * 50)
print("2. DESERIALIZATION: JSON → Python")
print("-" * 30)

json_input = '''
{
    "name": "Bob",
    "age": 25,
    "courses": ["Physics", "Chemistry"],
    "active": false
}
'''

python_obj = json.loads(json_input)
print("JSON string loaded:")
print(python_obj)
print(f"Name: {python_obj['name']}")
print(f"Age: {python_obj['age']}")
print(f"First course: {python_obj['courses'][0]}")

# ============================================================
# EXERCISE 3: Read/Write JSON Files
# ============================================================
print("\n" + "=" * 50)
print("3. FILE OPERATIONS")
print("-" * 30)

filename = "student.json"
student_data = {
    "name": "Charlie",
    "age": 22,
    "courses": ["Programming", "Databases"],
    "grades": {"Math": 85, "Physics": 90}
}

with open(filename, "w") as f:
    json.dump(student_data, f, indent=4)
print(f"✓ Data written to {filename}")

with open(filename, "r") as f:
    loaded_data = json.load(f)
print("✓ Data loaded from file")
print(loaded_data)

# ============================================================
# WORKING WITH LISTS
# ============================================================
print("\n" + "=" * 50)
print("4. WORKING WITH LISTS")
print("-" * 30)

users = [
    {"name": "Alice", "age": 25, "city": "NY"},
    {"name": "Bob", "age": 30, "city": "LA"},
    {"name": "Charlie", "age": 22, "city": "Chicago"}
]

users_json = json.dumps(users, indent=2)
print("List of users as JSON:")
print(users_json)

with open("users.json", "w") as f:
    json.dump(users, f, indent=2)
print("\n✓ Users saved to users.json")

with open("users.json", "r") as f:
    loaded_users = json.load(f)
print(f"✓ Loaded {len(loaded_users)} users")

# ============================================================
# ERROR HANDLING
# ============================================================
print("\n" + "=" * 50)
print("5. ERROR HANDLING")
print("-" * 30)

invalid_json = '{"name": "Alice", "age": 25,}'  # Trailing comma

try:
    result = json.loads(invalid_json)
    print(result)
except json.JSONDecodeError as e:
    print(f"✓ Error caught: Invalid JSON format")
    print(f"  {e}")

# ============================================================
# CONFIGURATION EXAMPLE
# ============================================================
print("\n" + "=" * 50)
print("6. CONFIGURATION EXAMPLE")
print("-" * 30)

config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    }
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
print("✓ Configuration saved")

with open("config.json", "r") as f:
    loaded_config = json.load(f)
print(f"✓ App: {loaded_config['app_name']} v{loaded_config['version']}")
print(f"  Database: {loaded_config['database']['host']}:{loaded_config['database']['port']}")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 50)
print("JSON METHODS SUMMARY")
print("-" * 30)

methods = [
    ("json.dumps()", "Python object → JSON string"),
    ("json.dump()",  "Python object → JSON file"),
    ("json.loads()", "JSON string → Python object"),
    ("json.load()",  "JSON file → Python object")
]

for method, desc in methods:
    print(f"  {method:12} - {desc}")

# ============================================================
# CLEANUP
# ============================================================
print("\n" + "=" * 50)
print("CLEANUP")
print("-" * 30)

files_to_remove = ["student.json", "users.json", "config.json"]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"✓ Removed {file}")

print("\n" + "=" * 50)
print("LAB WORK COMPLETED")
print("=" * 50)
import csv
import os

print("FILE HANDLING LABORATORY")
print("=" * 50)

# ============================================================
# EXERCISE 1: Basic Text File Operations
# ============================================================
print("\n1. TEXT FILE OPERATIONS")
print("-" * 30)

file1 = "sample.txt"
text_content = """Hello, world!
This is a sample text file.
It contains multiple lines of text for testing file operations."""

with open(file1, "w") as f:
    f.write(text_content)
print(f"✓ File '{file1}' created")

with open(file1, "r") as f:
    content = f.read()
print("\nFile content:")
print(content)

print("\nReading line by line:")
with open(file1, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")

# ============================================================
# EXERCISE 2: CSV File Operations
# ============================================================
print("\n" + "=" * 50)
print("2. CSV FILE OPERATIONS")
print("-" * 30)

csv_file = "people.csv"
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
print(f"✓ CSV file '{csv_file}' created")

print("\nReading CSV file:")
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

print("\nUsing DictReader:")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']} is {row['Age']} from {row['City']}")

# ============================================================
# EXERCISE 3: Appending to Files
# ============================================================
print("\n" + "=" * 50)
print("3. APPENDING TO FILES")
print("-" * 30)

with open(file1, "a") as f:
    f.write("\nThis line is appended to the file.")
print(f"✓ Data appended to '{file1}'")

with open(file1, "r") as f:
    updated = f.readlines()
print("\nUpdated file (last 2 lines):")
for line in updated[-2:]:
    print(f"  {line.strip()}")

# ============================================================
# ADDITIONAL OPERATIONS
# ============================================================
print("\n" + "=" * 50)
print("4. ADDITIONAL OPERATIONS")
print("-" * 30)

# Safe file creation
try:
    with open("new_file.txt", "x") as f:
        f.write("This is a new file.")
    print("✓ New file created with 'x' mode")
except FileExistsError:
    print("File already exists")

# Append to CSV
new_row = [["David", "28", "San Francisco"]]
with open(csv_file, "a", newline="") as f:
    csv.writer(f).writerows(new_row)
print("✓ New row added to CSV")

# Verify CSV append
with open(csv_file, "r") as f:
    row_count = sum(1 for _ in csv.reader(f))
print(f"  CSV now has {row_count} rows")

# File information
if os.path.exists(file1):
    size = os.path.getsize(file1)
    print(f"  File size: {size} bytes")

# ============================================================
# FILE MODES SUMMARY
# ============================================================
print("\n" + "=" * 50)
print("FILE MODES SUMMARY")
print("-" * 30)

modes = [
    ("'r'", "Read (default)"),
    ("'w'", "Write (overwrites)"),
    ("'a'", "Append"),
    ("'x'", "Create (fails if exists)"),
    ("'r+'", "Read and write"),
    ("'b'", "Binary mode")
]

for mode, desc in modes:
    print(f"  {mode:4} - {desc}")

print("\n" + "=" * 50)
print("LAB WORK COMPLETED")
print("=" * 50)

# Optional cleanup (uncomment if needed)
# os.remove("sample.txt")
# os.remove("people.csv")
# os.remove("new_file.txt")
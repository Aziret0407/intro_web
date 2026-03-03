nums = [10, 20, 30, 40, 50]

nums += [60]
nums.insert(1, 15)

if 30 in nums:
    nums.remove(30)

nums = nums[::-1]
nums = sorted(nums)

print("Final list:", nums)

print("First 3:", nums[:3])
print("Last 2:", nums[-2:])
print("Reversed copy:", list(reversed(nums)))

student_info = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}

student_info.update({"subject": "Math"})
student_info["grade"] = "A+"

if "age" in student_info:
    del student_info["age"]

print("Keys:", list(student_info.keys()))
print("Values:", list(student_info.values()))
print("Items:", list(student_info.items()))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_result = set_a | set_b
intersection_result = set_a & set_b
difference_result = set_a - set_b

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)

colors_tuple = ("red", "blue", "green", "red", "yellow")

print("Index of green:", colors_tuple.index("green"))
print("Count of red:", colors_tuple.count("red"))

company_data = {
    "employees": [
        {"name": "Dan", "position": "Master", "salary": 500000},
        {"name": "Jack", "position": "Bachelor", "salary": 10000}
    ]
}

new_employee = {
    "name": "Alex",
    "position": "Manager",
    "salary": 150000
}

company_data["employees"].append(new_employee)

for emp in company_data["employees"]:
    print(emp["name"])
employee = {
    "name": "Ravi",
    "salary": 45000
}

print(employee.get("salary", "Salary not found"))
print(employee.get("age", "Age not found"))

employee_1 = {
    "id": 101,
    "name": "Ravi",
    "salary": 45000
}

print(employee_1.keys())
print(employee_1.values())
print(employee_1.items())
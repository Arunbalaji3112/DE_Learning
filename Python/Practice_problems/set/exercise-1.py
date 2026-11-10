employee_ids = {101, 102, 103, 104, 105}

# 1. Add 106 using add().

employee_ids.add(106)
print(employee_ids)
# 2. Add 107, 108, 109 using update().

employee_ids.update({107, 108, 109})
print(employee_ids)
# 3. Remove 103 using remove().
employee_ids.remove(103)
print(employee_ids)
# 4. Try discard(999) and observe whether an error occurs.
employee_ids.discard(999)
print(employee_ids)
# 5. Check whether 105 exists using in.
if 105 in employee_ids:
    print("105 exists in the set.")
# 6. Create a copy of the Set.
emp_cpy=employee_ids.copy()
print(emp_cpy)
# 7. Clear the original Set.
employee_ids.clear()
# 8. Print both the original and copied Sets.

print(employee_ids)
print(emp_cpy)
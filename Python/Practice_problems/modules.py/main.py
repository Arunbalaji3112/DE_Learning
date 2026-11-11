import employee_utils

Actual_salary = 50
emp_name=employee_utils.clean_name(" ARUNBALAJI     ")
Bonus_salary = employee_utils.add_bonus(Actual_salary)

print(emp_name)
print(Bonus_salary)
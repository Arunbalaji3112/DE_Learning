salaries = [30000, 40000, 50000, 60000, 70000]

high_salaries = list(
    filter(lambda salary: salary > 50000, salaries)
)

print(high_salaries)
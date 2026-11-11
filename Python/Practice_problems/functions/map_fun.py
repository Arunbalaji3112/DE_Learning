num=[1,2,3,4,5,1]

new_num = map(lambda x:x*5,num)
print(list(new_num))


employees = [    {"name": " ravi ", "salary": 45000},    {"name": " PRIYA ", "salary": 65000},    {"name": " arun ", "salary": 55000},    {"name": " mohan ", "salary": 35000}]


# 1. Clean all employee names.
# 2. Keep only employees earning at least ₹50,000.

clean_emp = map(lambda emp: {"emp_name": emp["name"].strip().title(), "salary": emp["salary"]}, employees)
high_earners = list(filter(lambda emp: emp["salary"] >= 50000, clean_emp))
print(high_earners)

numbers = [10, 20, 30]

def double(x):
    print("Processing:", x)
    return x * 2

result = map(double, numbers)
print("Map created")
print(next(result))  # Process the first item
# print(list(result))
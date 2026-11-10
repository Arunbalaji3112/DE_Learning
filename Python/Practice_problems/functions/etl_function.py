raw_customers = [
    {"id": "101", "name": " RAVI ", "salary": "45000"},
    {"id": "102", "name": " priya ", "salary": "65000"},
    {"id": "103", "name": " ARUN ", "salary": "55000"}
]
def clean_name(name):
    return name.strip().title()

def convert_salary(salary):
    return int(salary)

def transform_customer(record):
    return {
        "id": int(record["id"]),
        "name": clean_name(record["name"]),
        "salary": convert_salary(record["salary"])
    }

cleaned_customers = []

for customer in raw_customers:
    cleaned_customers.append(transform_customer(customer))

print(cleaned_customers)
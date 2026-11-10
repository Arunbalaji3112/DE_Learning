records = [
    ("Chennai", "2026-11-05", 15000),
    ("Mumbai", "2026-11-05", 20000),
    ("Chennai", "2026-11-06", 18000)
]

# for city, date, amount in records:
#     print(city, date, amount)

sales = {}

for city, date, amount in records:
    sales[(city, date)] = amount

print(sales)
print(sales[("Mumbai", "2026-11-05")])
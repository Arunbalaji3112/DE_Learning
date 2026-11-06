# Without using a loop, write Python code to:

orders = [101, 102, 103, 102, 104, 105, 102]


# 1. Count how many times order ID 102 appears.

count_102=orders.count(102)
print(count_102)
# 2. Find the index of the first 102.

index_102=orders.index(102)
print(index_102)
# 3. Remove only the first occurrence of 102.
orders.pop(index_102)
print(orders)           
# 4. Sort the list in descending order.
orders.sort(reverse=True)
# 5. Create a copy of the sorted list.
orders_copy=orders.copy()
# 6. Clear the original list and prove that the copied list still contains the order IDs.
orders.clear()
print(orders)
print(orders_copy)


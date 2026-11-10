incoming_ids = [101, 102, 103, 101, 104, 102, 105]
existing_ids = [101, 103, 106]


# 1. Convert both Lists into Sets.
print("Unique incoming customer IDs:", set(incoming_ids))
print("Existing customer IDs:", set(existing_ids))
# 2. Print the unique incoming customer IDs.
print("Unique incoming customer IDs:", set(incoming_ids))
# 3. Find new customer IDs not present in the existing data.
new_customer_ids = set(incoming_ids).difference(set(existing_ids))
print("New customer IDs not present in existing data:", new_customer_ids)
# 4. Find incoming customer IDs already present in existing data.
new_in_exist= set(incoming_ids).intersection(set(existing_ids))
print("Incoming customer IDs already present in existing data:", new_in_exist)
# 5. Print the number of unique incoming IDs.
print("Number of unique incoming IDs:", len(set(incoming_ids)))
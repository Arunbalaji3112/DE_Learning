yesterday = {101, 102, 103, 104}
today = {103, 104, 105, 106}

#union operation bring unique values fro both sets
print(yesterday.union(today))

#Intersection operation bring common values from both sets
print(yesterday.intersection(today))

#diffrence operation bring values from first set which are not present in second set
print(yesterday.difference(today))

#symmetric difference operation bring values from both sets which are not present in both sets
print(yesterday.symmetric_difference(today))
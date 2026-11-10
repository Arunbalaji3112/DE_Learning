yesterday = {101, 102, 103, 104}
today = {103, 104, 105, 106}

#union operation bring unique values fro both sets
print(yesterday.union(today))
# print(yesterday | today)

#Intersection operation bring common values from both sets
print(yesterday.intersection(today))
# print(yesterday & today)
#diffrence operation bring values from first set which are not present in second set
print(yesterday.difference(today))
# print(yesterday - today)

#symmetric difference operation bring values from both sets which are not present in both sets
print(yesterday.symmetric_difference(today))
# print(yesterday ^ today)

#update() opeartion in existing set

yesterday.update(today)
print(yesterday)

#intersection_update() in existing set

yesterday.intersection_update(today)
print(yesterday)

#difference_update() in existing set
yesterday.difference_update(today)
print(yesterday)

#symmetric_difference_update() in existing set
yesterday.symmetric_difference_update(today)
print(yesterday)
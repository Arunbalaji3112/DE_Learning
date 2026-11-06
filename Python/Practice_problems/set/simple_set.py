# Sets can help identify distinct values in a small or moderately sized dataset.
# For very large distributed datasets, you would typically use SQL DISTINCT or PySpark distinct().
"""Sets are useful for local Python processing,
 but in a large-scale ETL pipeline, SQL or PySpark joins are usually 
more appropriate because they can operate on data that doesn't fit in one Python process's memory"""
#Set to set
num = {1,1,2,3,4,4,5,6,7,7,8,8,9,5,67,67,63,32,32}
print(type(num))
unique_num= set(num)
print(type(unique_num))
print(unique_num)

#tuple to set
num = (1,1,2,3,4,4,5,6,7,7,8,8,9,5,67,67,63,32,32)
print(type(num))
unique_num = set(num)
print(type(unique_num))
print(unique_num)

# List to set
num = [1,1,2,3,4,4,5,6,7,7,8,8,9,5,67,67,63,32,32]
print(type(num))
unique_num = set(num)
print(type(unique_num))
print(unique_num)

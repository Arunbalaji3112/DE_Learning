numbers = (10, 20, 30, 40)

# 1. Try to change the value at index 1 to 200.
#  numbers[1]=200

# 2. Observe the error.
# Traceback (most recent call last):
#   File "F:\DE_Learning\Python\Practice_problems\tuples\exercise-2.py", line 4, in <module>
#     numbers[1]=200
#     ~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# 3. Create a new tuple containing the original numbers plus 50.
num_numbers=numbers+(50,)
print(num_numbers)
# 4. Print both tuples to show that the original was not modified.
print(numbers)  
print(num_numbers)
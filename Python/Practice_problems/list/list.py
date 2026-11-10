# Python List complexity cheat sheet
# ------------------Fast operations
# - Access by index: O(1)
# - Get length: O(1)
# - Append at end: O(1) amortized
# - Pop from end: O(1)

#------------------Potentially expensive operations
# - Search for a value: O(n)
# - Insert at beginning: O(n)
# - Remove by value: O(n)
# - Pop from beginning: O(n)
# - Iterate through all elements: O(n)
# - Sort: O(n log n)
# - Slice: O(k) time and space
num = [1, 2, 3, 4, 5,5] 
print(num)

#Append an element to the end of the list
num.append(6)

#Extend the list by appending elements from another iterable
num.extend([7,8,9])

#Insert an element at a specific index
num.insert(9,10)

#remove the first occurrence of a value
num.remove(10)

#pop an element at a specific index
num.pop(8)
print(num)

#index of the first occurrence of a value
print("a")
print(num)
index_find=num.index(9)
print(index_find)
num.pop(index_find)
print(num)

#count the number of occurrences of a value
print("a")
print(num.count(9))

#sort the list in ascending order
num.sort()
print(num)

#sort the list in descending order
num.sort(reverse=True)
print(num)

#copy the list
num_copy=num.copy()
print(num_copy)

#reverse the elements of the list in place
num.reverse()

#remove all elements from the list
num.clear()

# print(num)
# for i in num:
#     print(i)
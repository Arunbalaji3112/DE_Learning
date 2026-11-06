#Method 1: add()

a={1,2,3,4}

a.add(5)
a.add(4)

print(a)

#Notice that adding 20 again does not create a duplicate.

# PS F:\DE_Learning\Python\Practice_problems\set> py .\set_inbuilt_methods.py
# {1, 2, 3, 4, 5}

#Method 2: update()

a.update({6,7,8})
print(a)
print(type(a))

#Method 3: remove()

a.remove(8)
print(a)

#Method 4: discard()

a.discard(7)
print(a)

#Method 5: pop()

a.pop()
print(a)

#Method 7: clear()

# a.clear()
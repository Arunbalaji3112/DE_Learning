salary = [1,2,"a","invalid"]


# try:
#     for i in salary:
#      sal = int(i)
#      print("Salary:", sal)
# except ValueError:
#     print("Invalid salary detected",salary[i])

# print("Program continues")

for i in salary:
    try:
        sal = int(i)
        print("Salary:", sal)
    except ValueError:
        print("Invalid salary detected:", i)

print("Program continues")
# Type                              Example	            Description
# 1. No parameters, no return	        greet()	        Performs an action

def greet():
    print("Hello, welcome to the Python program!")

greet()  # Calling the function to see the output

# 2. Parameters, no explicit return	greet("Ravi")	Uses input and prints
def greet(Name):
    print("My name is:",Name)

greet("Arunbalaji")  # Calling the function with a parameter to see the output
# 3. No parameters, returns value	    get_status()	Produces a result

def greet():
    return "I am 25 year old who learning python to become a Data Engineer"

greeting = greet()  # Calling the function and storing the return value
print(greeting)  # Printing the returned value

# 4. Parameters and return	            add(10, 20)	    Processes input and returns result

def greet(a,b):
    c= a+b
    return c

add = greet(10,20)  # Calling the function with parameters and storing the return value
print(add)  # Printing the returned value
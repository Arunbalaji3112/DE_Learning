def numbers():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")
    yield 30

gen = numbers()
print(gen)

print(next(gen))  # Start, 10
print(next(gen))  # Middle, 20
print(next(gen))  # End, 30
def count_occurrences(numbers, target):
    count = 0

    for n in numbers:
     if n == target:
            count += 1

    return count


num = [101, 102, 103, 102, 104, 105, 102,101]

result = count_occurrences(num, 101)

print(result)
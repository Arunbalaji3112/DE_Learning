num=[101, 102, 103, 102, 104, 105, 102]
count_102=num.count(102)
print(count_102)

index_102=num.index(102)
print(index_102)
print(len(num))

for i in range(len(num)):
    if num[i]==102:
        num.pop(i)
        break
print(num)
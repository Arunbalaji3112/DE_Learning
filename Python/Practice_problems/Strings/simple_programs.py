customers = [
    "  RAVI  ",
    "priya",
    " ARUN ",
    "mOhAn"
]

#remove the lead and taili space from elements of list

new_cus=[]
for i in customers:
    new_cus.append(i.strip().title())
print(new_cus)
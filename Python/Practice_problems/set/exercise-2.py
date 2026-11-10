aws_team = {101, 102, 103, 104, 105}
data_team = {103, 104, 105, 106, 107}


# 1. All unique employees across both teams.

print("All unique employees across both teams:", aws_team.union(data_team))
# 2. Employees working in both teams.
print("Employees working in both teams:", aws_team.intersection(data_team))
# 3. Employees working only in the AWS team.
print("Employees working in AWS teams",aws_team.difference(data_team))
# 4. Employees working only in one of the two teams.
print("Employees working only in one of the two teams:", aws_team.symmetric_difference(data_team))
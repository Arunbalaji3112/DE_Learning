# Exercise 3 — Data Engineering function

# Write a function named etl_summary() that returns three values:
# - Total records: 5000
# - Successful records: 4950
# - Failed records: 50
# Unpack the returned tuple into three variables and print the results.

def etl_summary():
       Total_records = 5000
       Successful_records= 4950
       Failed_records= 50
       average_success_rate = Successful_records / Total_records * 100
       average_failure_rate = Failed_records / Total_records * 100
       
       return Total_records, Successful_records, Failed_records ,average_success_rate,average_failure_rate

 

total, successful, failed,*others= etl_summary()
print("Total records:", total)
print("Successful records:", successful)
print("Failed records:", failed)

#This is called extended iterable unpacking.

print("Average success rate & failure rate:", others)
print("Average success rate & failure rate:", others[0], others[1])
print("Average success rate & failure rate:", others[0:2])
# print("Average failure rate:", average_failure_rate)

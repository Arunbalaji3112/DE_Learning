customers = [    "  ravi@gmail.com  ",    " PRIYA@GMAIL.COM ",    "  Arun@Yahoo.Com  ",    "MOHAN@OUTLOOK.COM "]


# 1. Removes leading and trailing whitespace from every email.

trimmed_list =[]
for i in customers:
    trimmed_list.append(i.strip())
    
print(trimmed_list)
# 2. Converts all emails to lowercase.
lower_text_list=[]
for i in trimmed_list:
    lower_text_list.append(i.lower())

print(lower_text_list)

# 3. Stores the cleaned emails in a new list called cleaned_emails.

cleaned_emails = lower_text_list.copy()

print(cleaned_emails)

# 4. Prints the original list and the cleaned list separately.

print(customers)
print(cleaned_emails)
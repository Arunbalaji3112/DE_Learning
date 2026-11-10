customers = [    "  RAVI@GMAIL.COM  ",    "priya@gmail.com",   
             "  ARUN@YAHOO.COM ",    "invalidemail",    " MOHAN@OUTLOOK.COM ",    "",    "  ",    "ravi@gmail.com"]

"""
1. Remove leading and trailing whitespace.
2. Convert every email to lowercase.
3. Skip empty strings after cleaning.
4. Keep only strings containing both @ and . (a basic check, not full email validation).
5. Remove duplicate emails.
6. Store the final emails in cleaned_emails."""


#Uncleaned customer data:
print("Original list of emails:", customers)
print("\n")

# 1. Remove leading and trailing whitespace & lower the elementys of list.
trimmed_lower_list = []
for email in customers:
    trimmed_lower_list.append(email.strip().lower())

print("Trimmed and lowercased emails:", trimmed_lower_list)

# 2. Skip empty strings after cleaning.
non_empty_list = []
for i in trimmed_lower_list:
    if i != "":
        non_empty_list.append(i)
print("Non-empty emails:", non_empty_list)

#3. Keep only strings containing both @ and . (a basic check, not full email validation).

special_char = ['@', '.']
speacial_char_contained_mail_list = []

for i in customers:
    if special_char[0] in i and special_char[1] in i:
        speacial_char_contained_mail_list.append(i.lower().strip())

print(speacial_char_contained_mail_list)

# 5. Remove duplicate emails.
remove_dup_email= set(speacial_char_contained_mail_list.copy())

print("Unique emails:",remove_dup_email)
# 6. Store the final emails in cleaned_emails.
cleaned_emails = list(remove_dup_email)
cleaned_emails.sort()
print("Final cleaned emails:", cleaned_emails)

print(range(3))
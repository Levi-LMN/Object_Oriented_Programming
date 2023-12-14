# logical operators are used to combine conditional statements
# There are three logical operators in Python:
# and
# or
# not

# and
# returns True if both statements are true
# returns False if one of the statements is false
# Example:
# if applicant has high income AND good credit
#     Eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# or
# returns True if one of the statements is true
# returns False if both statements are false
# Example:

has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# not
# returns True if the statement is false
# returns False if the statement is true
# Example:
# if applicant has good credit and does not have a criminal record
#     Eligible for loan

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

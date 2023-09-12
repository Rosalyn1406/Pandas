import pandas as pd
from tabulate import tabulate

users_email_df = pd.read_csv('users_email.csv')
# print(users_email_df)

# define function 
def valid_emails(users_email: pd.DataFrame) -> pd.DataFrame:
    # Filter the valid emails with conditions

    # [a-zA-Z] -> first character of the email address which should be a letter(uppercase/lowercase)
    # [a-zA-Z0-9._%+-]* -> This part matches the rest of the characters in the username part of the email. 
    # It can include letters (uppercase or lowercase), digits, underscores, periods, percent signs, plus signs, and dashes. 
    # The * means that there can be zero or more occurrences of these characters.

    # @: This symbol matches the literal "@" character in the email address.
    # but the domain here wants is @leetcode.com
    # @[a-zA-Z0-9.-]+ -> This part matches the domain name part of the email address. 
    # It can include letters (uppercase or lowercase), digits, periods, and dashes. 
    # The + means that there must be at least one occurrence of these characters.

    #\. -> This part matches the literal period (dot) character in the domain name.
    # [a-zA-Z]{2,} ->  This part matches the top-level domain (TLD) of the email address, which consists of letters (uppercase or lowercase) 
    # and should be at least two characters long.

    # $: This symbol signifies the end of the string.


    valid_emails_df = users_email[users_email['email'].str.contains(r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$')]

    # select the column and rows you wish to display 
    # return in any order
    result_df = valid_emails_df[['user_id','name','email']]

    return result_df

final_result = valid_emails(users_email_df)
print(final_result)

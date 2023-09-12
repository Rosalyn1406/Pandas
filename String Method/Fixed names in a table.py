import pandas as pd
from tabulate import tabulate

users_df = pd.read_csv('users.csv')

print(users_df)

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
     # Set the conditions whereby we must change the first character to uppercase and the rest lowercase
     # uses the .str.capitalize() method to apply the capitalize() function element-wise to each string in the 'name' column
     # It correctly transforms each name string to have the first character capitalized and the rest in lowercase.
    users['name'] = users['name'].str.capitalize()

    # Select the columm that we like to display 
    result_df = users[['user_id','name']]

    # use sort_values for ascending order for the user id
    result_df_ascending = result_df.sort_values(by='user_id', ascending=True)

    return result_df_ascending

# Take the changed user_df DataFrame into the fix_names function to display the new output
final_result = fix_names(users_df)
print(tabulate(final_result, headers='keys', tablefmt ='psql'))

## users_capitalize_df = users[users['name'].capitalize()]:
## This line attempts to use the capitalize() function directly on the entire 'name' column, treating it as a condition for filtering rows. 
## However, the capitalize() function is not a condition; it's meant to be applied to individual strings, not entire columns.
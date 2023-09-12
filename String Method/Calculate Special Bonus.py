import pandas as pd
from tabulate import tabulate

# bonus = employee_id is odd number, name does not start with M
# no bonus = employee_id is even, start with M

employees_df = pd.read_csv('employees.csv')

# print(employees_df)

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # Create a new column for 'bonus' in the emplyoyess DataFrame with default value 0
    employees['bonus'] = 0 

    # Filter rows whereby bonus = salary if employee_id is odd and name does not start with M
    bonus_condition = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))
    # bonus_df = employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']


    # Filter the original DataFrame employees using this condition to get a new DataFrame employees_with_bonus that only contains the rows of eligible employees.
    # This creates a condition that evaluates to True for the eligible employees and False for others.
    employees_with_bonus = employees[bonus_condition]
    
    # Assign the salary values to the 'bonus' column for eligible employees
    # using .loc, you can apply this condition to select the rows where the bonus_condition is True
    # update the 'bonus' column with the corresponding 'salary' values:
    # .loc is used to locate (select) rows and columns in a DataFrame based on labels or conditions and then apply changes to those selected rows and columns.
    employees.loc[bonus_condition,'bonus'] = employees_with_bonus['salary']
   
    # Select only the required columns and sort the result table by emplyee_id in ascending order
    result_df = employees[['employee_id','bonus']].sort_values(by='employee_id', ascending=True)

    return result_df

# Shorter version 
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # Create a new column for 'bonus' in the emplyoyess DataFrame with default value 0
    employees['bonus'] = 0 

    # Filter rows whereby bonus = salary if employee_id is odd and name does not start with M
    bonus_df = employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
   
    # Select only the required columns and sort the result table by emplyee_id in ascending order
    result_df = employees[['employee_id','bonus']].sort_values(by='employee_id', ascending=True)

    return result_df

# Taking employees_df csv file into the calculate_special_bonus function to print output
final_result = calculate_special_bonus(employees_df)

print(tabulate(final_result,headers='keys', tablefmt ='psql'))
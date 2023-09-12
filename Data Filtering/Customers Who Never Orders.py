# Find all customers who never order anything
# if the customerID does not apper in the order table that means they did order anything. 

import pandas as pd
from tabulate import tabulate

# Load data from a CSV file
# def load_customers_table_data():
customers_df = pd.read_csv("Customers.csv")
orders_df = pd.read_csv("Orders.csv")

# Print the data from the csv file
# print(customers_df)
# print(orders_df)

# Filter and select desired columns 
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_with_order = orders['customerId'].unique()

    # select and filter the rows which 'id' is not present in orders['customersID']
    # isin(values) is used to filter and select rows based on whether their values are present in a given set(values).
    # ~ represent logical negation


    # Use boolean indexing to filter the rows from the 'customers' DataFrame.
    # The condition checks if the 'id' column in the customers DataFrame is not present in the 'customerId' column of the 'order' DataFrame.
    # the (~) negates the result, meaning we select only rows where the 'id' is not found in the 'customerId' column of the orders DataFrame. 
    # Id 2 and 4 from customers DataFrame is not found in 'customersId' of the orders DataFrame. 

    customers_without_order = customers[~customers['id'].isin(orders['customerId'])]

    # we have to rename 'name' -> 'customers'
    # build a dataframe that only contains the column 'name'
    # rename the column 'name' as 'customer'
    # customers_without_order[['name']] -> selecting desired column (only 'name') from customer_without order. 
    new_DataFrame = customers_without_order[['name']].rename(columns={'name':'Customers'})
    
    return new_DataFrame

# Create new result dataframe using the find_customers function with customer and orders dataframe
result_df = find_customers(customers_df,orders_df)

# print and tabulate the result
print(tabulate(result_df, headers='keys', tablefmt='psql'))

# Approach number 2 

def find_customers_approach2(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
   # Merge the customers DataFrame with the orders DataFrame using left join on 'id' and 'customersId'
   merged_df = customers.merge(orders, how='left', left_on='id', right_on='customerId')

   # Use the 'consumerId' column to create a boolean mask for customers who never placed any order
   # Create a boolean mask named mask by checking if the 'customerId' column in the merged DataFrame is null. 
   # This mask will be True for customers who never placed any orders and False for customers who placed orders. 
   # merged_df[merged_df['customerId']] -> extracts the 'customerId' column from the (merged_df) DataFrame 
   # merged_df[merged_df['customerId']] -> merged_df is placed before square bracket to apply indexing boolean to the merged_df DataFrame

   mask = merged_df[merged_df['customerId'].isna()]

   # select on the 'name' column from the result DataFrame and rename it as 'Customers'
   # mask[['name']] -> Selecting the desired column (the one that we want to display) from mask DataFrame
   new_DataFrame = mask[['name']].rename(columns={'name':'Customers'})

   return new_DataFrame

# Take the find_customers_approach2 function as customer DataFrame and orders DataFrame as arguments 
result_merged_df = find_customers_approach2(customers_df,orders_df)

# Print and tabulate the result
print(tabulate(result_merged_df, headers='keys',tablefmt='psql'))






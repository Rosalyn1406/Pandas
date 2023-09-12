import pandas as pd
from tabulate import tabulate

# Loading csv file 
# def load_products_data():
#     products_df = pd.read_csv('products.csv')
#     return products_df

products_df = pd.read_csv('products.csv')

# Print to check the data in the excel file 
# print(load_products_data())

# Define DataFrame for new outputs(low fats and recyclable)
def find_products(products:pd.DataFrame) -> pd.DataFrame:

    # Filtering products that has low fats AND is recyclable
    products_id_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

    # Selecting the desired column(only product_id will be display) from the filtered products
    results_df = products_id_df[['product_id']]
    
    # Print and tabulate the result
    # This command alone won't print the result, need line of code 28 to display it. 
    # print(tabulate(results_df, headers='keys', tablefmt ='psql'))

    return results_df

# Display the output is low fats and is recyclable using find_products function using the latest csv data that has been filtered and selected
final_result = find_products(products_df)
print(tabulate(final_result, headers='keys', tablefmt ='psql'))


# Approach 2
# import pandas as pd
# from tabulate import tabulate

# # Load data from a CSV file
# products_data = pd.read_csv('products.csv')

# # Function definition without arguments
# def find_products():
#     # Since there's no argument, the function can't access products_data directly
#     # You would need to use the global variable products_data to access the loaded data

#     # For example, this would work:
#     products_id_df = products_data[(products_data['low_fats'] == 'Y') & (products_data['recyclable'] == 'Y')]
#     results_df = products_id_df[['product_id']]
    
#     # Tabulate and display the result
#     tabulated_result = tabulate(results_df, headers='keys', tablefmt='psql')
#     print(tabulated_result)

#     return results_df

# # Call the function
# find_products()











 



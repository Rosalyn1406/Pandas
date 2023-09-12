# To determine if the country is considered "big", there are two conditions to verify
# The country must have an area of at least three million square kilometres, denoted as area >= 3,000,000
# The population of the country should be a minimum of twenty-five million, as population >= 25,000,000

# Apply row filteting to identify the countries that satisfy the conditions
# df = world[(world['area'] >= 3000000)] | (world['population'] >= 25000000)]
# This step filters out the rows representing countries that do not meet the conditions, leaving the remaining table as follows

# Need to return three columns according to the requirements of the problem. 
# Next step is returning the three required columns with the relative order as: name, population, and area

import pandas as pd
from tabulate import tabulate

# Loading from a CSV file
def load_world_data():
    world_df = pd.read_csv('world.csv')
    return world_df

# Sample DataFrame (manually input)
# world = {'name': ['Afghanistan', 'Albania', 'Algeria','Andorra','Angola'],
#         'population': [25500100, 2831741, 37100000,78115,20609294],
#         'area': [652230, 28748, 2381741,468,1246700],
#         'continent':['Asia','Europe','Africa','Europe','Africa'],
#         'gdp':[20343000000,1296000000,188681000000,3721000000,10099000000]
#         }

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    # Filtering the big countries that satisfy the conditions
    big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]

    # Selecting the desired columns from the filtered countries (columns you want to display)
    result_df = big_countries_df[['name', 'population', 'area']]

    # Displaying the resulting DataFrame
    # Print a tabulated result using tabulate first then only return 
    # tablefmt = psql is the format of the table
    # headers ='keys' specifies that the table headers shoudl be the keys of the DataFrame.
    # -> It will display the column names as the first row of the table

    # print(tabulate(result_df,headers='keys', tablefmt='psql'))

    return result_df

# world_df = load_world_data()

# Display the big countries unsing big_countires function with csv data 
final_result = big_countries(load_world_data())

# print and tabulate the data 
print(tabulate(final_result, headers='keys', tablefmt='psql'))
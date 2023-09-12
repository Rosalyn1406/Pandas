import pandas as pd
from tabulate import tabulate

# Write a solution to find all the authors that viewed at least one of their own articles.
# Equal author_id and viewer_id indicate the same person.

# load csv data to read
views_df = pd.read_csv('views.csv')
print(views_df)

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    # author_id == viewer_id indicates the same person
    
    # Filter the rows with the condition where author_id is the same as viewer_id
    author_viewer_df = views[views['author_id'] == views['viewer_id']]

    # We need to extract the unique author_id values from the (views) DataFrame
    # We want to find the unique author who viewed at least one of their own articles
    # Result is in array 
    result_df = author_viewer_df['viewer_id'].unique()
    print(result_df)
    
    # Put it in ascending order for the result
    # Result is in array,not in DataFrame
    # Need to change to DataFrame first before applying sort_values() functions 
    # But we use sorted () function since it is an array 
    ascending_result = sorted(result_df)
    # result_df = sorted(result_df)

    # Now, we create a DataFrame from the sorted result (ascending_result)
    # DataFrame is create where the sorted array(ascending result) is assigned to a column named 'id'
    final_result_df = pd.DataFrame({'id':ascending_result})

    return final_result_df

# Calling the article_views function and using the latest csv file that has been filter and selected
final_result_table = article_views(views_df)

# Print and tabulate the final result 
print(tabulate(final_result_table, headers='keys', tablefmt='psql'))



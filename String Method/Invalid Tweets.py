# tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15
# result the table in any order

import pandas as pd
from tabulate import tabulate 

# Load csv file
tweets_df = pd.read_csv('tweets.csv')

# Print the csv file 
print(tweets_df)

# Define invalid_tweets function to filter and display specific result 
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    # Filter the rows with the condition where the number of characters used in the content of the tweet is greater than 15
    # Using str.len() to calculate the length of the character
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]

    # Selecting the desired column to be display ('tweet_id)
    result_df = invalid_tweets_df[['tweet_id']]

    # Return the result 
    return result_df

# Display the output taking the csv file into invalid_tweets function 
final_results = invalid_tweets(tweets_df)

# Tabulate the table of the output(tweet_id)
print(tabulate(final_results, headers='keys', tablefmt ='psql'))




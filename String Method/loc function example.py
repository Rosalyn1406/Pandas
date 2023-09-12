import pandas as pd

data = {
    'student_id': [1, 1, 2, 2, 3, 3],
    'subject': ['Math', 'English', 'Math', 'English', 'Math', 'English'],
    'score': [90, 85, 78, 92, 88, 76]
}

df = pd.DataFrame(data)
# print original dataframe
print(df)

# Change the score of student_id 2 in the subject 'English' to 95
# df.loc[(df['student_id'] == 2) & (df['subject'] == 'English'), 'score'] = 95

# Method 2 for clarity 
# Student_id 2 in the subject english 
condition = (df['student_id'] == 2) & (df['subject'] == 'English')

# Use .loc to select rows and column of new DataFrame and update the changes of score to 95
df.loc[condition,'score'] = 95

# print dataframe with the changes
print(df)



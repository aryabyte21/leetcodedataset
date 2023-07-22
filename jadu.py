import pandas as pd

questions_df = pd.read_csv('questions.csv')
solutions_df = pd.read_csv('solutions.csv')

merged_df = pd.merge(solutions_df, questions_df,
                     left_on='Question', right_on='id', how='inner')

new_df = merged_df[['Question', 'title', 'description', 'Answer']]

new_df.to_csv('merged_dataset.csv', index=False)

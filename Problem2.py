import pandas as pd
import math
from scipy import stats

# Load file
file_path = 'Project1Ziraddin.xlsx'
df = pd.read_excel(file_path)

# List of all unique description types
description_types = df['Description'].unique()

# We will perform pairwise t-tests for each of the description types
columns_to_compare = ['Deleted', 'Sent', 'Total']

# Initialize an empty list to store the results of the t-tests
t_test_results = []

# Iterate through all combinations of description types
for i in range(len(description_types)):
    for j in range(i + 1, len(description_types)):
        desc1 = description_types[i]
        desc2 = description_types[j]
        
        # Perform t-tests for each of the specified columns ('Deleted', 'Sent', 'Total')
        for column in columns_to_compare:
            # Filter data for each description type
            data1 = df[df['Description'] == desc1][column]
            data2 = df[df['Description'] == desc2][column]
            
            # Calculate the required statistics
            n1 = data1.count()
            n2 = data2.count()
            mean1 = data1.mean()
            mean2 = data2.mean()
            std1 = data1.std()
            std2 = data2.std()
            
            # Calculate pooled standard deviation
            pooled_std = math.sqrt((((n1 - 1) * std1**2) + ((n2 - 1) * std2**2)) / (n1 + n2 - 2))
            
            # Calculate t-value
            t_value = (mean1 - mean2) / (pooled_std * math.sqrt((1/n1) + (1/n2)))
            
            # Calculate degrees of freedom
            df_degrees_of_freedom = n1 + n2 - 2
            
            # Calculate p-value
            p_value = 2 * (1 - stats.t.cdf(abs(t_value), df_degrees_of_freedom))
            
            # Store the result
            t_test_results.append({
                'Description1': desc1,
                'Description2': desc2,
                'Column': column,
                'n1': n1,
                'n2': n2,
                'mean1': mean1,
                'mean2': mean2,
                'std1': std1,
                'std2': std2,
                't_value': t_value,
                'p_value': p_value
            })

# Convert the results into a DataFrame for easy viewing
t_test_results_df = pd.DataFrame(t_test_results)
print(t_test_results_df)

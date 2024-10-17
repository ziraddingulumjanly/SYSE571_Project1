import pandas as pd

file_paths = [
    '2011_simplified.csv',
    '2012_simplified.csv',
    '2013_simplified.csv',
    '2014_simplified.csv',
    '2015_simplified.csv',
    '2016_simplified.csv',
    '2017_simplified.csv'
]

# Load CSV files into a dictionary of dataframes
data_frames = {year: pd.read_csv(file_path) for year, 
               file_path in zip(range(2011, 2018), file_paths)}

# Combine all dataframes into one 
combined_df = pd.concat(data_frames.values()) # for the all 7 years statistics

# Initialize dictionaries to store results 
yearly_stats = {}
description_stats = {}

# Given columns are : Deleted, Sent, and Total

# PART1: Compute mean and std by year for given columns
for year, df in data_frames.items():
    yearly_stats[year] = {
        'Deleted_mean': df['Deleted'].mean(),
        'Deleted_std': df['Deleted'].std(),
        'Sent_mean': df['Sent'].mean(),
        'Sent_std': df['Sent'].std(),
        'Total_mean': df['Total'].mean(),
        'Total_std': df['Total'].std(),
    }

# PART2:Compute mean and std for all 7 years combined
combined_stats = {
    'Deleted_mean': combined_df['Deleted'].mean(),
    'Deleted_std': combined_df['Deleted'].std(),
    'Sent_mean': combined_df['Sent'].mean(),
    'Sent_std': combined_df['Sent'].std(),
    'Total_mean': combined_df['Total'].mean(),
    'Total_std': combined_df['Total'].std(),
}

# PART3: Compute mean and std by Description type for given columns
for description in combined_df['Description'].unique():
    df_description = combined_df[combined_df['Description'] == description]
    description_stats[description] = {
        'Deleted_mean': df_description['Deleted'].mean(),
        'Deleted_std': df_description['Deleted'].std(),
        'Sent_mean': df_description['Sent'].mean(),
        'Sent_std': df_description['Sent'].std(),
        'Total_mean': df_description['Total'].mean(),
        'Total_std': df_description['Total'].std(),
    }

# Display the results
def display_stats(stats, label):
    print(f"\n{label} Statistics:")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value:.2f}")

# Display yearly stats
for year, stats in yearly_stats.items():
    display_stats(stats, f"Year {year}")

# Display combined stats for all 7 years
display_stats(combined_stats, "Combined (All 7 years)")

# Display description-based stats
for description, stats in description_stats.items():
    display_stats(stats, f"Description: {description}")
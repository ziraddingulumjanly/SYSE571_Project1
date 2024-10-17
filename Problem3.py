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


data_frames = {year: pd.read_csv(file_path) for year, file_path in zip(range(2011, 2018), file_paths)}
combined_df = pd.concat(data_frames.values())

# Overall mean of the "Total" column across all years
overall_mean_total = combined_df['Total'].mean()

# Add a shifted column for the previous week's data for "Total" and "Description"
combined_df['Prev_Total'] = combined_df['Total'].shift(1)
combined_df['Prev_Description'] = combined_df['Description'].shift(1)

# Problem 3.1: 
# Conditional Probability for "Total" > 1500 in the previous week and its impact on current week being above/below the overall mean
def prob_total_above_below_mean_given_prev_total_above_1500(df, overall_mean):
    total_above_1500_prev = df[df['Prev_Total'] > 1500]
    above_mean = total_above_1500_prev[total_above_1500_prev['Total'] > overall_mean].shape[0]
    below_mean = total_above_1500_prev[total_above_1500_prev['Total'] <= overall_mean].shape[0]

    total_count = total_above_1500_prev.shape[0]
    return above_mean / total_count, below_mean / total_count

above_mean_prob, below_mean_prob = prob_total_above_below_mean_given_prev_total_above_1500(combined_df, overall_mean_total)

# Problem 3.2: 
# Conditional Probability for current week's Total being above/below the mean if the previous week was an "Announcement"
def prob_total_above_below_mean_given_prev_announcement(df, overall_mean):
    announcement_prev = df[df['Prev_Description'] == 'Announcement']
    above_mean = announcement_prev[announcement_prev['Total'] > overall_mean].shape[0]
    below_mean = announcement_prev[announcement_prev['Total'] <= overall_mean].shape[0]

    total_count = announcement_prev.shape[0]
    return above_mean / total_count, below_mean / total_count

announcement_above_mean_prob, announcement_below_mean_prob = prob_total_above_below_mean_given_prev_announcement(combined_df, overall_mean_total)

# Problem 3.3: 
# Using Bayes' theorem to calculate P(Normal | Total > 1500)
def bayesian_prob_normal_given_total_above_1500(df):
    # Probability of a "Normal" week
    p_normal = df[df['Description'] == 'Normal'].shape[0] / df.shape[0]
    
    # Probability of Total being above 1500
    p_total_above_1500 = df[df['Total'] > 1500].shape[0] / df.shape[0]
    
    # Probability of Total being above 1500 given it's a Normal week
    normal_weeks = df[df['Description'] == 'Normal']
    p_total_above_1500_given_normal = normal_weeks[normal_weeks['Total'] > 1500].shape[0] / normal_weeks.shape[0]
    
    # P(Normal | Total > 1500) 
    p_normal_given_total_above_1500 = (p_total_above_1500_given_normal * p_normal) / p_total_above_1500
    
    return p_normal_given_total_above_1500, p_normal, p_total_above_1500

bayes_result, p_normal, p_total_above_1500 = bayesian_prob_normal_given_total_above_1500(combined_df)

# Display the   results with descriotive sentences.
print("\nProblem 3.1: Conditional Probability if the previous week's Total was > 1500")
print(f"Probability of this week's Total being above the overall mean: {above_mean_prob:.4f}")
print(f"Probability of this week's Total being below the overall mean: {below_mean_prob:.4f}")

print("\nProblem 3.2: Conditional Probability if the previous week was an Announcement")
print(f"Probability of this week's Total being above the overall mean: {announcement_above_mean_prob:.4f}")
print(f"Probability of this week's Total being below the overall mean: {announcement_below_mean_prob:.4f}")

print("\nProblem 3.3: Bayes' Theorem - Probability of a Normal week given Total > 1500")
print(f"P(Normal | Total > 1500) = {bayes_result:.4f}")
print(f"P(Normal) = {p_normal:.4f}")
print(f"P(Total > 1500) = {p_total_above_1500:.4f}")




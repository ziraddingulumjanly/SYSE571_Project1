import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'Project1Ziraddin.xlsx'
xls = pd.ExcelFile(file_path)

# Load the first sheet and filter data for years between 2011 and 2017
df = pd.read_excel(xls, sheet_name='Project1_EntireDataset_Ziraddin')
df_filtered = df[(df['Year'] >= 2011) & (df['Year'] <= 2017)]

# Group by year and week, then calculate the sum of 'Sent', 'Deleted', and 'Total'
df_grouped = df_filtered.groupby(['Year', 'Week']).agg({'Sent': 'sum', 'Deleted': 'sum', 'Total': 'sum'}).reset_index()

# Clean data by ensuring 'Sent' and 'Deleted' columns are numeric
df_grouped_clean = df_grouped.copy()
df_grouped_clean['Sent'] = pd.to_numeric(df_grouped_clean['Sent'], errors='coerce')
df_grouped_clean['Deleted'] = pd.to_numeric(df_grouped_clean['Deleted'], errors='coerce')

# Grouping the data by week and year to calculate the average for 'Deleted', 'Sent', and 'Total'
df_avg_by_week = df_grouped_clean.groupby(['Week', 'Year']).mean().reset_index()

# Using a new color palette for better distinction between years
palette = sns.color_palette("tab10", n_colors=len(df_avg_by_week['Year'].unique()))

# Set up the figure and axes for the subplots
fig, axes = plt.subplots(3, 1, figsize=(14, 18))

# Plot for 'Deleted' emails with improved palette and visibility
sns.barplot(x='Week', y='Deleted', hue='Year', data=df_avg_by_week, ax=axes[0], palette=palette)
axes[0].set_title('')
axes[0].set_xlabel('Week of the Year')
axes[0].set_ylabel('Average Deleted Emails')
axes[0].legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
axes[0].tick_params(axis='x', rotation=45)

# Plot for 'Sent' emails
sns.barplot(x='Week', y='Sent', hue='Year', data=df_avg_by_week, ax=axes[1], palette=palette)
axes[1].set_title('')
axes[1].set_xlabel('Week of the Year')
axes[1].set_ylabel('Average Sent Emails')
axes[1].legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
axes[1].tick_params(axis='x', rotation=45)

# Plot for 'Total' emails
sns.barplot(x='Week', y='Total', hue='Year', data=df_avg_by_week, ax=axes[2], palette=palette)
axes[2].set_title('')
axes[2].set_xlabel('Week of the Year')
axes[2].set_ylabel('Average Total Emails')
axes[2].legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

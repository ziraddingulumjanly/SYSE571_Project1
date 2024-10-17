import pandas as pd
import matplotlib.pyplot as plt

# Load the provided Excel file
file_path = 'Project1Ziraddin.xlsx'
xls = pd.ExcelFile(file_path)

# Load the specific sheet into a DataFrame
project1_data = pd.read_excel(xls, sheet_name='Project1_EntireDataset_Ziraddin')

# Filter data to include only years from 2011 to 2017
filtered_data = project1_data[project1_data['Year'].between(2011, 2017)]

# Create line plots for each email metric ('Deleted', 'Sent', 'Total') across weeks from 2011-2017
plt.figure(figsize=(10, 6))

# Create a line plot for each year
for year in filtered_data['Year'].unique():
    year_data = filtered_data[filtered_data['Year'] == year]
    plt.plot(year_data['Week'], year_data['Total'], label=str(year))

# Set plot labels and title
plt.title('Weekly Total Emails (2011-2017)')
plt.xlabel('Week')
plt.ylabel('Total Emails')
plt.legend(title='Year')

# Show the plot
plt.tight_layout()
plt.show()

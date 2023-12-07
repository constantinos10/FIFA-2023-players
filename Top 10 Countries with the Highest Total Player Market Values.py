import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('fifa_2023_players.csv')

# Group the data by nationality and calculate the sum of player market values for each country
country_values = df.groupby('nationality_name')['value_eur'].sum()

# Sort the countries based on total player market value in descending order
sorted_countries = country_values.sort_values(ascending=False)

# Select the top 10 countries with the highest total player market values
top_10_countries = sorted_countries.head(10)

# Plot the bar chart for the top 10 countries
top_10_countries.plot(kind='bar')

# Set title and labels for the plot
plt.title('Top 10 Countries with the Highest Total Player Market Values')
plt.xlabel('Country')
plt.ylabel('Total Player Market Value (EUR)')

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('fifa_2023_players.csv')

# Group the data by league and get the mean wage of each league
wage_mean = df.groupby('league_name')['wage_eur'].mean()

# Plot the bar chart
wage_mean.plot(kind='bar')

# Set the title and labels
plt.title('Average Player Wage per League')
plt.xlabel('League')
plt.ylabel('Average Wage (EUR)')

# Show the plot
plt.show()

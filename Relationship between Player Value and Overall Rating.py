import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and store it in a DataFrame 'df'
df = pd.read_csv("fifa_2023_players.csv")

# Create a scatter plot between 'overall' and 'value_eur' columns
df.plot.scatter(x='overall', y='value_eur', s=50, c='blue')

# Add labels and title to the plot
plt.xlabel("Overall")
plt.ylabel("Value in EUR")
plt.title("Relationship between Player Value and Overall Rating")

# Show the plot
plt.show()

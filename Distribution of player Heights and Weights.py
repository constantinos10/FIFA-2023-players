import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the csv file into a DataFrame 'df'
df = pd.read_csv("fifa_2023_players.csv")

# Create a scatter plot for player heights and weights
plt.scatter(df['height_cm'], df['weight_kg'])

# Add labels and a title to the plot
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Distribution of Player Heights and Weights")

# Show the plot
plt.show()

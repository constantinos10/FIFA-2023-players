import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and store it in a DataFrame 'df'
df = pd.read_csv("fifa_2023_players.csv")

# Group the data by league name and count the number of players in each league
grouped = df.groupby("league_name").count()["player_id"]

# Plot the bar chart
grouped.plot(kind="bar", color="blue", figsize=(15, 5))

# Add labels and title to the chart
plt.xlabel("League Name")
plt.ylabel("Number of Players")
plt.title("Number of Players per League")

# Show the plot
plt.show()
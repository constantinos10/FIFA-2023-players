import pandas as pd
import matplotlib.pyplot as plt

# Load the FIFA 2023 players dataset
df = pd.read_csv("fifa_2023_players.csv")

# Count the number of players in each country
country_counts = df["nationality_name"].value_counts()

# Select the top 10 countries
top_10_countries = country_counts.head(10)

# Plot the top 10 countries as a bar chart
top_10_countries.plot(kind='bar')

# Add labels and title to the chart
plt.xlabel("Country")
plt.ylabel("Number of Players")
plt.title("Top 10 Countries with the Most Players in FIFA 2023")

# Show the chart
plt.show()

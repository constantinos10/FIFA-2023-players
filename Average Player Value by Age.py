import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv("fifa_2023_players.csv")

# Calculate the average value for each age group and plot the line chart
df.groupby("age")["value_eur"].mean().plot(kind='line')

# Set labels and title for the plot
plt.xlabel("Age")
plt.ylabel("Average Value (EUR)")
plt.title("Average Player Value by Age")

# Show the plot
plt.show()

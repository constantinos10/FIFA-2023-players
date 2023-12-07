import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
df = pd.read_csv('fifa_2023_players.csv')

# Group the data by skill moves and count the number of players in each group
grouped = df['skill_moves'].value_counts()

# Create a pie chart to show the proportion of players with different skill move ratings
plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Players with Different Skill Move Ratings')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()

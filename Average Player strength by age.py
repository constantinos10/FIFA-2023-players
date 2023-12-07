import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and handle mixed data types warning by setting low_memory=False
df = pd.read_csv('fifa_2023_players.csv', low_memory=False)

# Calculate the average overall score by age
mean_overall_by_age = df.groupby('age')['overall'].mean()

# Plot the average overall score by age
plt.plot(mean_overall_by_age.index, mean_overall_by_age, 'o-', color='blue')

# Add labels and title to the plot
plt.xlabel('Age')
plt.ylabel('Average Overall Score')
plt.title('Average Player Strength by Age')

# Show the plot
plt.show()

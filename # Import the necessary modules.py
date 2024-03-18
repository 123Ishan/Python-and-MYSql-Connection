# Import the necessary modules
import MySQLdb
import matplotlib.pyplot as plt

# Assuming myvars is a dictionary that contains your database credentials
myvars = {
    'DB username': 'svchaita',
    'DB password': 'artificer mg intermarriage',
    'DB databasename': 'svchaita_db'
}

# Connect to the database
conn = MySQLdb.connect(host="localhost",
                       user=myvars['DB username'],
                       passwd=myvars['DB password'],
                       db=myvars['DB databasename'])
cursor = conn.cursor()

# Execute SQL queries and fetch the data
# A. Fetch the top 5 weeks with the highest average quiz scores
cursor.execute("""
    SELECT Week, AvgQuizScores
    FROM StudentPerformance
    ORDER BY AvgQuizScores DESC
    LIMIT 5
""")
result_a = cursor.fetchall()

# B. Retrieve the trend of average study hours over the weeks
cursor.execute("""
    SELECT Week, AvgStudyHours
    FROM StudentPerformance
    ORDER BY Week
""")
result_b = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Function to plot the results
def plot_results(result_a, result_b):
    # Plot A: Top 5 Weeks with the Highest Average Quiz Scores
    weeks_a, scores = zip(*result_a)  
    plt.figure(figsize=(10, 5))
    plt.barh(weeks_a, scores, color='skyblue')
    plt.xlabel('Average Quiz Scores')
    plt.ylabel('Weeks')
    plt.title('Top 5 Weeks with the Highest Average Quiz Scores')
    plt.gca().invert_yaxis()
    plt.show()

    # Plot B: Trend of Average Study Hours Over the Weeks
    weeks_b, study_hours = zip(*result_b)  
    plt.figure(figsize=(10, 5))
    plt.plot(weeks_b, study_hours, marker='o', linestyle='-', color='purple')
    plt.xlabel('Weeks')
    plt.ylabel('Average Study Hours')
    plt.title('Trend of Average Study Hours Over the Weeks')
    plt.grid(True)
    plt.show()

# Call the function to plot the results
plot_results(result_a, result_b)
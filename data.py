import csv
import pandas as pd
import mysql.connector

# Convert the text file to CSV with headers
df = pd.read_csv('record.txt', header=None)
df.columns = ['Name', 'Status']
df.to_csv('RECORDCSV.csv', index=False)

# Connect to the MySQL database (make sure 'hangman' DB exists!)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="word_guessing_game"
)
cursor = db.cursor()

# Read and insert the CSV into the MySQL table
with open('RECORDCSV.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO RECORD(USER, STATUS) VALUES (%s, %s)", row)

db.commit()
cursor.close()
db.close()

print("Written successfully!")

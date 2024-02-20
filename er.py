import sqlite3
import random
import os

# Define database name
db_name = 'myDatabase.db'

# Connect to the SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS Names (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS Cities (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                City TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS RandomData (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Data TEXT NOT NULL)''')

# Function to generate sample data
def generate_data():
    names = [f'Name_{i}' for i in range(1, 1001)]
    cities = [f'City_{i}' for i in range(1, 101)]
    random_data = [f'RandomData_{i}' for i in range(1, 101)]
    return names, cities, random_data

# Insert data into the database
def insert_data(conn, names, cities, random_data):
    c = conn.cursor()
    for name in names:
        c.execute("INSERT INTO Names (Name) VALUES (?)", (name,))
    for city in cities:
        c.execute("INSERT INTO Cities (City) VALUES (?)", (city,))
    for data in random_data:
        c.execute("INSERT INTO RandomData (Data) VALUES (?)", (data,))
    conn.commit()

# Generate sample data
names, cities, random_data = generate_data()

# Insert generated data into the database
insert_data(conn, names, cities, random_data)

# Close the connection
conn.close()

print("Data insertion complete.")

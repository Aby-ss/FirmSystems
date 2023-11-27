import sqlite3

# Connect to an SQLite database
conn = sqlite3.connect('Example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Name TEXT,
        Age INTEGER
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO Users (Name, Age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO Users (Name, Age) VALUES ('Bob', 30)")

# Commit changes and close the connection
conn.commit()
conn.close()

# Print the content of the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

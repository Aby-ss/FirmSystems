import sqlite3

from rich import print
from rich import text
from rich import box
from rich.panel import Panel
from rich.prompt import Prompt


from rich.traceback import install
install(show_locals=True)

# Connect to an SQLite database
conn = sqlite3.connect('Example.db')

name = Prompt.ask("Enter a Random Name ")
age = Prompt.ask("Enter a Random Age Integer ")

print(Panel.fit("Request Accepted!", box = box.SQUARE, border_style="bold green"))


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
cursor.execute(f"INSERT INTO Users (Name, Age) VALUES (?, ?)", (name, 25))
cursor.execute(f"INSERT INTO Users (Name, Age) VALUES (?, ?)", (name, 30))

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
